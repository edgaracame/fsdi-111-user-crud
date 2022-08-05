from flask import g
import sqlite3

DATABASE_URL_USERS = "user.db"
DATABASE_URL_VEHICLES = "vehicle.db"


def get_db_user():
    db = getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE_URL_USERS)
    return db


def get_db_vehicle():
    db = getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE_URL_VEHICLES)
    return db
