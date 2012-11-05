#-*- coding: utf-8 -*-

from functools import wraps
from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from utils import get_connection, make_datetime

def require_login(f):
    @wraps(f)
    def _(*args, **kw):
        if session['logged_in'] != True:
            flash('You were Not Logged in')
            return redirect(url_for('login'))
        return f(*args, **kw)
    return _

#> -------------------
#> Configuration
#> ------------------
USERNAME = 'xiaomo'
PASSWORD = '123'

master = Blueprint('master', __name__, static_folder='static', template_folder='templates')

@master.route('/')
@master.route('/index')
def show_entries():
    db = get_connection()
    entries = db.notes.find().sort('_id', -1).limit(20)
    return render_template('show_entries.html', entries=entries)

@master.route('/add', methods=['POST'])
@require_login
def add_entry():
    db = get_connection()
    db.insert({'text':request.form['text'], 'date': make_datetime()})
    flash('New Entry was successfully posted')
    return redirect(url_for('.show_entries'))

@master.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != USERNAME:
            error = 'Invalid Username'
        elif request.form['password'] != PASSWORD:
            error = 'Invalid Password'
        else:
            session['logged_in'] = True
            flash('You were Logged In')
            return redirect(url_for('.show_entries'))
    return render_template('login.html', error=error)

@master.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were Logged Out')
    return redirect(url_for('.show_entries'))

@master.route('/test')
def test():
    return str(url_for('.static', filename='style.css'))
