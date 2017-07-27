# -*- coding: utf-8 -*-
# quiz-orm/app.py

from flask import Flask, g
from peewee import SqliteDatabase
import os

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    DATABASE=os.path.join(app.root_path, 'quiz.db'),
    TYTUL='Quiz ORM Peewee'
))

# tworzymy instancję bazy używanej przez modele
baza = SqliteDatabase(app.config['DATABASE'])


@app.before_request
def before_request():
    g.db = baza
    g.db.get_conn()


@app.after_request
def after_request(response):
    g.db.close()
    return response
