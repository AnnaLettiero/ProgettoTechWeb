#! /usr/bin/env python3
from datetime import datetime
from flask import Flask
from models import user, post, book, genere, generibook, review, db
#from forms import RegistrationForm
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
#Istanzio Bcrypt
bcrypt = Bcrypt()
#Istanzio LoginManager
login_manager = LoginManager()
#Questo ci serve per le pagine che richiedono un accesso ad utente
#1. View da caricare nel caso in cui sia richiesto il login
#2. Come deve apparire il messaggio nella view di login
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dbannaksenia:dbannaksenia@localhost/DatabaseAnnaKsenia'
db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
from Progetto import routes