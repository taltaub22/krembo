from krembo import db
from models import Users
from models import Mentors
from models import Students
from models import Activities
from models import Transports
from models import TransportsToActivities
from models import StudentsInTransports


db.create_all()

db.session.add(Users("Tal","Taub","taltaub22@gmail.com","123456"))

db.session.commit()

