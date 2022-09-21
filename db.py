import psycopg2
from flask import g


def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            host="ec2-18-209-78-11.compute-1.amazonaws.com",
            database="d8khc8qncpickk",
            user="acokgqwvgersbr",
            password="a8d821d0ea3b6ae64c735df9ba0dd451e93a86ff1dc0a3a82dcd2de3e4c3756d")
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
