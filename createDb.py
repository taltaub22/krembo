import bcrypt
from flask_sqlalchemy import SQLAlchemy
from krembo import db
from models import *

db.drop_all()
db.session.commit()

db.create_all()
db.session.commit()

password = "123456"
salt = bcrypt.gensalt(5)
hashed_password = bcrypt.hashpw(password, salt)

tal = Users("Tal", "Taub", "taltaub22@gmail.com", hashed_password, salt)
db.session.add(tal)
db.session.commit()
