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
    data = {
        'title': 'Tower',
        'description': 'Tower is a custom apparatus designed and built by Junhee Won, an undergraduate scientist and engineer in KAIST. Tower Dashboard is supporting service of Tower, providing control of extruder/fiber motors and heater via web service.',
        'user': current_user
    }
    return render_template('index.html', data=data)

# @app.route(pathPrefix + '/login', methods=['POST'])
# def login():
#     
#     return jsonify(json_res)

@app.route(pathPrefix + '/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        data = {'duplicate_username': False}
        return render_template('signup.html', data=data)
    
    user_id = request.form['username']
    password = request.form['password']
    if user_id in USERS:
        data = {'duplicate_username': True}
        return render_template('signup.html', data=data)
    addUser(User(user_id, passwd_hash=password))
    return redirect(url_for('login'))

@app.route(pathPrefix + '/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if current_user.is_anonymous:
            data = {
                'title': 'Tower',
                'wrong_credential': False
            }
            return render_template('login.html', data=data)
        return redirect(url_for('dashboard'))

    user_id = request.form['username']
    password = request.form['password']
    if user_id not in USERS:
        data = {
            'wrong_credential': True,
            'alert_text': "Wrong username or password."
        }
        return render_template('login.html', data=data)
    elif not USERS[user_id].can_login(password):
        data = {
            'wrong_credential': True,
            'alert_text': "Wrong username or password."
        }
        return render_template('login.html', data=data)
    elif not USERS[user_id].authorized:
        data = {
            'wrong_credential': True,
            'alert_text': "Unauthorized."
        }
        return render_template('login.html', data=data)
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

@app.route(pathPrefix + '/users', methods=['GET', 'POST'])
@login_required
def users():
    if request.method == 'GET':
        user = current_user
        data = {
            'users': USERS,
            'master': user.master
        }
        return render_template('users.html', data=data)
    
    user_id = request.form['username']
    authorize = request.form['authorize']

    if user_id in USERS:
        authorizeUser(USERS[user_id], authorize=='true')
        return '', 200
    else:
        return '', 404

@app.route(pathPrefix + '/dashboard')
@login_required
def dashboard():
    inputs = [
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
    if current_user.authorized:
        data = {
            'title': sitename,
            'inputs': inputs
        }
        return render_template('dashboard.html', data=data)
    else:
        return redirect(url_for('login'))


if __name__ == "__main__":
    api = Api(app)
    api.add_resource(Heater, '/api/heater')
    api.add_resource(Extruder, '/api/extruder')
    api.add_resource(Fiber, '/api/fiber')
    app.run(host='0.0.0.0', port=int(os.environ['TOWER_WEB_PORT']))