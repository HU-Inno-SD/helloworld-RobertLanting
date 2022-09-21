import sqlite3

def init_db():
    sqlite3.connect("flaskr.sqlite").execute(
    "create table challenges (id integer primary key autoincrement,"
    " name text,"
    " description text,"
    " start_date text,"
    " end_date text,"
    " done text)")