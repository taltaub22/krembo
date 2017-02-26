import bcrypt
from flask_sqlalchemy import SQLAlchemy
from krembo import db
from models import *

#droping all db
db.drop_all()
db.session.commit()


#crating my db
db.create_all()
db.session.commit()

#Creating admin user
password = "123456"
salt = bcrypt.gensalt(5)
hashed_password = bcrypt.hashpw(password, salt)

tal = Users("Tal", "Taub", "taltaub22@gmail.com", hashed_password, salt)
db.session.add(tal)
db.session.commit()
