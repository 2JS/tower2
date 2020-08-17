from flask import *
# import tower

pathPrefix = ""

app = Flask(__name__)

# if (pathPrefix):
#     @app.route('/')
#     def redirect_root():
#         return redirect(url_for('root'))

@app.route(pathPrefix + '/')
def index():
    return render_template('index.html')

@app.route(pathPrefix + '/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)