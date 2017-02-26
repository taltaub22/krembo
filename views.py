from flask import render_template


def index(title="Home"):
    return render_template("MainTamplate.html", title=title)


def login():
    return render_template("Login.html")

