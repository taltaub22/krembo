from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index(title="Home"):
    return render_template("MainTamplate.html",title=title)


if __name__ == '__main__':
    app.run()
