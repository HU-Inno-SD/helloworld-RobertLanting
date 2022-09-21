import sqlite3

from flask import g


def init_db():
    sqlite3.connect("flaskr.sqlite").execute(
    "create table challenges (id integer primary key autoincrement,"
    " name text,"
    " description text,"
    " start_date text,"
    " end_date text,"
    " done text)")

def get_db():
    if 'db' not in g:
        init_db()
        g.db = sqlite3.connect("flaskr.sqlite")
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
