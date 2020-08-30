from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import sqlite3

# create the application object
app = Flask(__name__)
# config
import os

app.config.from_object(os.environ['APP_SETTINGS'])
# app.secret_key = "skodo"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# create sqlalchemy objects
db = SQLAlchemy(app)

# import db schema
from models import *


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('you need to login first.')
            return redirect(url_for('login'))

    return wrap


# use decorators to link the fxn to a url
@app.route('/')
@login_required
def home():
    # return "Hello, World!"  # return a string
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)  # render a template


@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'invalid login credentials. please try again'
        else:
            session['logged_in'] = True
            flash('you were just logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('you were just logged out')
    return redirect(url_for('welcome'))


# connect to database
def connect_db():
    return sqlite3.connect('posts.db')


# start the server with the run() method
if __name__ == '__main__':
    app.run(debug=True)
