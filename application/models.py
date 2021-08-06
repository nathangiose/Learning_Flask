import flask
from application import db


class User(db.Document):
    user_id = db.IntField(unique=True)
    first_name = db.StringField(max_length=25)
    last_name = db.StringField(max_length=25)
    email = db.StringField(max_length=30)
    password = db.StringField(max_length=255)


class Course(db.Document):
    course_id = db.StringField(max_length=10, unique=True)
    title = db.StringField(max_length=100)
    description = db.StringField(max_length=100)
    credits = db.IntField()
    terms = db.StringField(max_length=25)


class Enrollment(db.Document):
    user_id = db.IntField()
    course_id = db.StringField(max_length=10)
