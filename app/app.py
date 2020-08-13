from flask import Flask
# import tower


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
