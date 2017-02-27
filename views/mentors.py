# encoding: utf-8
from flask import flash
from flask import render_template
from flask import request

from models import Mentors
from index import login_required


@login_required
def insert_mentor(title='הוסף חונך'):
    if request.method == 'POST':
        first_name = request.form['first_name'].strip()
        last_name = request.form['last_name'].strip()
        school = request.form['school'].strip()
        address = request.form['address'].strip()
        phone = request.form['phone'].strip()
        shirtsize = request.form['shirtSize'].strip()
        if first_name == "" or last_name == "" or school == "" or address == "" or phone == "" or shirtsize == "":
            flash('אולי שכחת למלא את אחד מהשדות?', 'alert-danger')
            return render_template('mentors/insert-mentor.html', title=title)
        mentor = Mentors(first_name, last_name, school, address, phone, shirtsize)
        from krembo import db
        db.session.add(mentor)
        db.session.commit()
    return render_template('mentors/insert-mentor.html', title=title)


@login_required
def view_mentors(title='חונכים'):
    mentors = Mentors.query.all()
    return render_template('mentors/view-mentors.html', title=title, mentors=mentors)
