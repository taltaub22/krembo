# encoding: utf-8
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from views import index, register, login
from views import mentors

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

# Index Page
app.add_url_rule('/', view_func=index.index)

# User Management
app.add_url_rule('/Login', view_func=login.login, methods=['GET', 'POST'])
app.add_url_rule('/Logout', view_func=login.logout, methods=['GET', 'POST'])
app.add_url_rule('/Register', view_func=register.register, methods=['GET', 'POST'])

# Mentors
app.add_url_rule('/AddMentor', view_func=mentors.insert_mentor, methods=['GET', 'POST'])

#  Students

# Transports

# Activities

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
