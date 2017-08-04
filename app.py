
from flask import Flask
from flask import request
from flask import abort
from flask import redirect
felm flask import Response
from flask import url_for

from flask.ext.login import LoginManager
from flask.ext.login import login_required
from flask.ext.login import UserMixin
from flask.ext.login import login_user

app = Flask(__name__)


@app.route('/')
def main():
    return redirect(url_for('login'))
    
@app.route('/login')
def index():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/hello')
def index():
	return "<h2>Hello World</h2>"

@app.route('/home')
@login_required
def home():
	return "<h1>User Home</h1>"

 