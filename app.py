from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello friends, Its my first docker container from docker image'

@app.route('/home')
def health():
    return 'Enjoy you are at your home!'
