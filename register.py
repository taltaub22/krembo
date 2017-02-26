# encoding: utf-8
import bcrypt
from flask import Flask, session, redirect, render_template, url_for
from flask import flash
from flask import request
from flask_sqlalchemy import SQLAlchemy

import login
from models import *


def register(title='רישום'):
    if 'logged_in' in session:
        if request.method == 'POST':
            email = request.form['email'].strip()
            first_name = request.form['first_name'].strip()
            last_name = request.form['last_name'].strip()
            password = request.form['password'].strip()
            if email == "" or first_name == "" or last_name == "" or password == "":
                flash("לא מילאת את אחד או יותר מהפרטים!")
                return render_template("Register.html", title=title)
            if login.user_exists(email):
                flash("הדואר האלקטרוני שבחרת כבר תפוס!")
                return render_template("Register.html", title=title)
            salt = bcrypt.gensalt(5)
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
            user = Users(first_name, last_name, email, hashed_password, salt)
            db.session.add(user)
            db.session.commit()
        return render_template("Register.html", title=title)
    else:
        return redirect(url_for('index'))
