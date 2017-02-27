# encoding: utf-8
from functools import wraps

from flask import redirect
from flask import render_template
from flask import session
from flask import url_for


def index(title="דף הבית"):
    return render_template("index.html", title=title)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)

    return decorated_function
