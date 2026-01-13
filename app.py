from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/home')
def health():
    return 'Enjoy you are at your home!'
