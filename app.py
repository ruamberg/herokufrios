from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template

from flask import Response, request, session, abort
from flask.ext.login import LoginManager, UserMixin, login_required, login_user, logout_user

app = Flask(__name__)

@app.route('/')
def main():
    return redirect(url_for('login'))
    
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')