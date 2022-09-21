import sqlite3

from flask import g

from app import app


def init_db():
    db = get_db()

    with app.open_resource('db/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))



def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect("flaskr.sqlite")
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
