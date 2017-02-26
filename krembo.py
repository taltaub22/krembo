# encoding: utf-8
import os
from flask import Flask
from flask import request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

import views
import Login


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/Login', view_func=Login.login,methods=['GET', 'POST'])

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

