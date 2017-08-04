from flask import Flask
from flask import render_template
from flask import redirect

app = Flask(__name__)

@app.route('/')
def main():
    return redirect(http://webfrios.herokuapp.com/login)

@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/login')
def login():
    return render_template('login.html')
    