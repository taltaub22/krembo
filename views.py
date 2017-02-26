# encoding: utf-8
from flask import render_template


def index(title="דף הבית"):
    return render_template("MainTamplate.html", title=title)




