# encoding: utf-8
import bcrypt
from flask import Flask, session, redirect, render_template, url_for
from flask import flash
from flask import request
from flask_sqlalchemy import SQLAlchemy
from models import *


def login():
    if 'logged_in' not in session:
        if request.method == 'POST':
            email = request.form['userName'].strip().lower()
            password = request.form['pass'].strip()
            if not user_exists(email):
                flash('משתמש לא קיים במערכת', 'alert-danger')
                return render_template('Login.html', title="התחברות")
            return check_login(email, password)

    return render_template('Login.html', title="התחברות")


def user_exists(entered_email):
    if Users.query.filter_by(email=entered_email).first() is not None:
        return True
    return False


def check_login(entered_email, entered_password):
    user = Users.query.filter_by(email=entered_email).first()
    if user is not None:
        salt = user.salt.encode('utf-8')
        if user.password == bcrypt.hashpw(entered_password.encode('utf-8'), salt):
            session['logged_in'] = True
            return redirect(url_for('index'))
    return render_template(url_for('login'), title="התחברות")


def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
        return redirect(url_for('index'))
    return redirect(url_for('login'))
