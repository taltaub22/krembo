from flask_sqlalchemy import SQLAlchemy
from krembo import db


class Users(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.String(80))
    lastName = db.Column(db.String(80))
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, id, first_name, last_name, email, password):
        self.id = id
        self.firstName = first_name
        self.lastName = last_name
        self.email = email
        self.password = password

    def __init__(self, first_name, last_name, email, password):
        self.firstName = first_name
        self.lastName = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<user %r' % self.email


class Mentors(db.Model):
    __tablename__ = 'Mentors'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    school = db.Column(db.String(80))
    address = db.Column(db.String(150))
    phone = db.Column(db.String(12))
    shirtSize = db.Column(db.String(5))

    def __init__(self, id, first_name, last_name, school, address, phone, shirt_size):
        self.id = id
        self.firstName = first_name
        self.lastName = last_name
        self.school = school
        self.address = address
        self.phone = phone
        self.shirtSize = shirt_size

    def __repr__(self):
        return '<mentor %r>' % self.firstName + " " + self.lastName


class Students(db.Model):
    __tablename__ = 'Students'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.String(80))
    lastName = db.Column(db.String(80))
    address = db.Column(db.String(150))
    contactName = db.Column(db.String(80))
    contactPhone = db.Column(db.String(12))
    photoApproval = db.Column(db.Boolean, default=False)
    wheelChair = db.Column(db.Boolean)
    comment = db.Column(db.String(200))

    def __init__(self, id, first_name, last_name, address, contact_name, contact_phone, photo_approval, wheel_chair,
                 comment):
        self.id = id
        self.firstName = first_name
        self.lastName = last_name
        self.address = address
        self.contactName = contact_name
        self.contactPhone = contact_phone
        self.photoApproval = photo_approval
        self.wheelChair = wheel_chair
        self.comment = comment

    def __repr__(self):
        return '<student %r>' % self.firstName + " " + self.lastName


class Activities(db.Model):
    __tablename__ = 'Activities'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject = db.Column(db.String(150))
    date = db.Column(db.DateTime)

    def __init__(self, id, subject, date):
        self.id = id
        self.subject = subject
        self.date = date

    def __repr__(self):
        return '<activity %r>' % self.id + " " + self.subject


class Transports(db.Model):
    __tablename__ = 'Transports'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    color = db.Column(db.String(20))
    amountOfWheelChairs = db.Column(db.Integer)
    amountOfStudents = db.Column(db.Integer)
    area = db.Column(db.String(150))

    def __init__(self, id, color, amount_of_wheel_chairs, amount_of_students, area):
        self.id = id
        self.color = color
        self.amountOfWheelChairs = amount_of_wheel_chairs
        self.amountOfStudents = amount_of_students
        self.area = area

    def __repr__(self):
        return '<Transportation %r>' % self.id + " " + self.color


class TransportsToActivities(db.Model):
    __tablename__ = 'TransportsToActivities'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    transportId = db.Column(db.Integer, db.ForeignKey('Transports.id'))
    activityId = db.Column(db.Integer, db.ForeignKey('Activities.id'))
    direction = db.Column(db.Integer)

    def __init__(self, id, transport_id, activity_id, direction):
        self.id = id
        self.transportId = transport_id
        self.activityId = activity_id
        self.direction = direction

    def __repr__(self):
        return '<TransportToActivities %r' % self.id + " " + self.direction


class StudentsInTransports(db.Model):
    __tablename__ = 'StudentsInTransports'

    studentId = db.Column(db.Integer, db.ForeignKey('Students.id'), primary_key=True)
    transportId = db.Column(db.Integer, db.ForeignKey('Transports.id'), primary_key=True)

    def __init__(self, student_id, transport_id):
        self.studentId = student_id
        self.transportId = transport_id

    def __repr__(self):
        return '<StudentsInTransports %r>' % self.studentId + " " + self.transportId


class MentorsInTransport(db.Model):
    __tablename__ = 'MentorsInTransport'

    mentorId = db.Column(db.Integer, db.ForeignKey('Mentors.id'), primary_key=True)
    transportsToActivitiesId = db.Column(db.Integer, db.ForeignKey('TransportsToActivities.id'), primary_key=True)

    def __init__(self, mentor_id, transports_to_activities_id):
        self.mentorId = mentor_id
        self.transportsToActivitiesId = transports_to_activities_id

    def __repr__(self):
        return '<MentorsIntransport %r>' & self.mentorId + " " + self.transportsToActivitiesId
