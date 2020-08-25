import os
from flask import *
# import tower
from api import *

pathPrefix = os.environ['TOWER_PATHPREFIX']
sitename = "Tower"

app = Flask(__name__)

# if (pathPrefix):
#     @app.route('/')
#     def redirect_root():
#         return redirect(url_for('root'))


@app.route(pathPrefix + '/')
def index():
    return redirect(url_for('dashboard'))

@app.route(pathPrefix + '/dashboard')
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