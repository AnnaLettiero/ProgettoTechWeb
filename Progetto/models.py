from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from Progetto import db, login_manager
from flask import current_app
from flask_login import UserMixin
db = SQLAlchemy()


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    usertype = db.Column(db.String(255), nullable=False)
    posts = db.relationship('Posts', backref='author')
    books = db.relationship('Books', backref='user')
    reviews = db.relationship('Reviews', backref='author')

class Posts(db.Model):
    __tablename__ = 'posts'
    idpost = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    coduser = db.Column(db.Integer, db.ForeignKey(
        'users.id'), nullable=False)


class Books(db.Model):
    __tablename__ = 'books'
    idbook = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    releasedate = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    publisher = db.Column(db.String(255), nullable=False)
    coduser = db.Column(db.Integer, db.ForeignKey(
        'users.id'), nullable=False)
    reviews = db.relationship('Reviews', backref='book') 


class Reviews(db.Model):
    __tablename__ = 'reviews'
    idreview = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(30), nullable=False)
    content = db.Column(db.Text, nullable=False)
    coduser = db.Column(db.Integer, db.ForeignKey(
        'users.id'), nullable=False)
    codbook = db.Column(db.Integer, db.ForeignKey(
        'books.idbook'), nullable=False)
    reviewdate = db.Column(db.DateTime, nullable=False,
                    default=datetime.utcnow)


class Generi(db.Model):
    __tablename__ = 'generi'
    idgenere = db.Column(db.Integer, primary_key=True)
    genere = db.Column(db.String(255), nullable=False)


class Generibooks(db.Model):
    __tablename__ = 'generibooks'
    idgenerebook = db.Column(db.Integer, primary_key=True)
    codgenere = db.Column(db.Integer, db.ForeignKey('generi.idgenere'), nullable=False)
    codbook = db.Column(db.Integer, db.ForeignKey('books.idbook'), nullable=False)
	