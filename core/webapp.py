from flask import Flask
app = None


def __init__(dst):
    global app
    app = Flask(__name__, static_folder=dst, static_url_path='/static')


@app.route('/')
def hello_world():
    return {'key': 'Hello, World!'}