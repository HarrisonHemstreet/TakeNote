from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    #date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

class users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship("Note")

"""

CREATE TABLE Note (
	id BIGSERIAL NOT NULL PRIMARY KEY,
	data VARCHAR(50) NOT NULL,
    user_id INT REFERENCES users
);

CREATE TABLE users (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    email VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(150) NOT NULL,
    first_name VARCHAR(150) NOT NULL
)

"""