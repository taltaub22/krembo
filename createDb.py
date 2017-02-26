from flask_sqlalchemy import SQLAlchemy
from krembo import db
from models import Users
from models import Mentors
from models import Students
from models import Activities
from models import Transports
from models import TransportsToActivities
from models import StudentsInTransports

db.drop_all()
db.create_all()

tal = Users("Tal", "Taub", "taltaub22@gmail.com", "123456", "ab$%#$42")
db.session.add(tal)
db.session.commit()
