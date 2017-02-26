import bcrypt
from flask import Flask, session, redirect, render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from models import *


def user_exists(enterd_email):
    if Users.query.filter_by(email=enterd_email).first() is not None:
        return True
    return False


def check_login(enterd_email, enterd_password):
    user = Users.query.filter_by(email=enterd_email).first()
    if user is not None:
        salt = user.salt
        if user.password is bcrypt(salt + enterd_password):
            session['logged_in'] = True
            return redirect(url_for('index'))
    return render_template(url_for('\Login'),errors=True)