import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.String(80))
    lastName = db.Column(db.String(80))
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, id, firstName, lastName, email, password):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password

    def __repr__(self):
        return '<user %r' % self.email


class Mentors(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    school = db.Column(db.String(80))
    address = db.Column(db.String(150))
    phone = db.Column(db.String(12))
    shirtSize = db.Column(db.String(5))

    def __init__(self, id, firstName, lastName, school, address, phone, shirtSize):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.school = school
        self.address = address
        self.phone = phone
        self.shirtSize = shirtSize

    def __repr__(self):
        return '<mentor %r>' % self.firstName + " " + self.lastName


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.String(80))
    lastName = db.Column(db.String(80))
    address = db.Column(db.String(150))
    contactName = db.Column(db.String(80))
    contactPhone = db.Column(db.String(12))
    photoApproval = db.Column(db.Boolean, default=False)
    wheelChair = db.Column(db.Boolean)
    comment = db.Column(db.String(200))

    def __init__(self, id, firstName, lastName, address, contactName, contactPhone, photoApproval, wheelChair, comment):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.contactName = contactName
        self.contactPhone = contactPhone
        self.photoApproval = photoApproval
        self.wheelChair = wheelChair
        self.comment = comment

    def __repr__(self):
        return '<student %r>' % self.firstName + " " + self.lastName


class Activities(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject = db.Column(db.String(150))
    date = db.Column(db.DateTime)

    def __init__(self, id, subject, date):
        self.id = id
        self.subject = subject
        self.date = date

    def __repr__(self):
        return '<activity %r>' % self.id + " " + self.subject


class Transportations(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    color = db.Column(db.String(20))
    amountOfWheelChairs = db.Column(db.Integer)
    amountOfStudents = db.Column(db.Integer)
    area = db.Column(db.String(150))

    def __init__(self, id, color, amountOfWheelChairs, amountOfStudents, area):
        self.id = id
        self.color = color
        self.amountOfWheelChairs = amountOfWheelChairs
        self.amountOfStudents = amountOfStudents
        self.area = area

    def __repr__(self):
        return '<Transportation %r>' % self.id + " " + self.color


