import os
from flask import *
from flask_login import *
from api import *
from user import *

pathPrefix = os.environ['TOWER_PATHPREFIX']
sitename = "Tower"

app = Flask(__name__)

app.secret_key = os.urandom(24)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def user_loader(user_id):
    return USERS[user_id]

# if (pathPrefix):
#     @app.route('/')
#     def redirect_root():
#         return redirect(url_for('root'))


@app.route(pathPrefix + '/')
def index():
    return redirect(url_for('login'))

# @app.route(pathPrefix + '/login', methods=['POST'])
# def login():
#     
#     return jsonify(json_res)

@app.route(pathPrefix + '/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html', duplicate_username=False)
    
    user_id = request.form['username']
    password = request.form['password']
    if user_id in USERS:
        return render_template('signup.html', duplicate_username=True)
    USERS[user_id] = User(user_id, passwd_hash=password)
    return redirect(url_for('login'))

@app.route(pathPrefix + '/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    user_id = request.form['username']
    password = request.form['password']
    if user_id not in USERS:
        # return render_template('login.html')
        return render_template('login.html', wrong_credential=True, alert_text="Wrong username or password.")
    elif not USERS[user_id].can_login(password):
        return render_template('login.html', wrong_credential=True, alert_text="Wrong username or password.")
    elif not USERS[user_id].authorized:
        return render_template('login.html', wrong_credential=True, alert_text="Unauthorized.")
    else:
        USERS[user_id].authenticated = True
        login_user(USERS[user_id], remember=True)
        return redirect(url_for('dashboard'))
    

@app.route(pathPrefix + '/logout', methods=['GET', 'POST'])
@login_required
def logout():
    user = current_user
    user.authenticated = False
    logout_user()
    return redirect(url_for('index'))

@app.route(pathPrefix + '/dashboard')
@login_required
def dashboard():
    metrics = [
        {
            "title": "Heater Temperature",
            "name": "heater",
            "unit": "˚C"
        },
        {
            "title": "Extruder Speed",
            "name": "extruder",
            "unit": "RPM"
        },
        {
            "title": "Fiber Speed",
            "name": "fiber",
            "unit": "RPM"
        }
    ]
    return render_template('dashboard.html', title=sitename+" - Dashboard", metrics=metrics)


if __name__ == "__main__":
    api = Api(app)
    api.add_resource(Heater, '/api/heater')
    api.add_resource(Extruder, '/api/extruder')
    api.add_resource(Fiber, '/api/fiber')
    app.run(host='0.0.0.0', port=int(os.environ['TOWER_WEB_PORT']))