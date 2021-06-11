# encoding: utf-8

from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)



    def __init__(self, *args, **kwargs):
        email = kwargs.get('email')
        username = kwargs.get('username')
        password = kwargs.get('password')

        self.email = email
        self.username = username
        self.password = generate_password_hash(password)

    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)
        return result


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # now()It's the first time the server runs and it's the same thing after that
    # now You get the current time every time you create a model
    create_time = db.Column(db.DateTime, default=datetime.now)
    comment = db.Column(db.Text, nullable=False)
    year = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)


    Booker_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    booker = db.relationship('User', backref='movie')

class Hall(db.Model):
    __tablename__ = 'hall'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))

    booker_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # The assigned relationship gets all the answers through Question and User (see what q&A the author has posted)
    movie = db.relationship('Movie', backref=db.backref('seats',
                                                      order_by=id.desc()))  # The comments are arranged in descending order of ID
    booker = db.relationship('Booker', backref=db.backref('seats'))

class Seat(db.Model):
    __tablename__ = 'seat'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    hall_id = db.Column(db.Integer, db.ForeignKey('hall.id'))
    booker_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # The assigned relationship gets all the answers through Question and User (see what q&A the author has posted)
    movie = db.relationship('Movie', backref=db.backref('seats',
                                                      order_by=id.desc()))  # The comments are arranged in descending order of ID
    booker = db.relationship('Booker', backref=db.backref('seats'))
