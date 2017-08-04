from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route('/')
def main():
    return redirect(url_for('login'))

@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/login')
def login():
    return render_template('login.html')
    