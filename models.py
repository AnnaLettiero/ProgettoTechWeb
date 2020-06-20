from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class user(db.Model):
    iduser = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    usertype = db.Column(db.String(255), nullable=False)


class post(db.Model):
    idpost = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    coduser = db.Column(db.Integer, db.ForeignKey(
        'user.iduser'), nullable=False)


class book(db.Model):
    idbook = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    releasedate = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    publisher = db.Column(db.String(255), nullable=False)
    coduser = db.Column(db.Integer, db.ForeignKey(
        'user.iduser'), nullable=False)


class review(db.Model):
    idreview = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(30), nullable=False)
    content = db.Column(db.Text, nullable=False)
    coduser = db.Column(db.Integer, db.ForeignKey(
        'user.iduser'), nullable=False)
    codbook = db.Column(db.Integer, db.ForeignKey(
        'book.idbook'), nullable=False)


class genere(db.Model):
    idgenere = db.Column(db.Integer, primary_key=True)
    genere = db.Column(db.String(255), nullable=False)


class generibook(db.Model):
	idgenerebook = db.Column(db.Integer, primary_key=True)
	codgenere = db.Column(db.Integer, db.ForeignKey('genere.idgenere'), nullable=False)
	codbook = db.Column(db.Integer, db.ForeignKey('book.idbook'), nullable=False)
	