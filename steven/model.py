"""
Steven personal webiste database API.
"""

import sqlite3
import flask
import steven

def dict_factory(cursor, row):
    """
    Converts database row object into a dictionary keyed on column name.

    This is useful for building dictionaries which are then used to render
    a template. Note that this would be inefficient for larger queries.
    """
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}


def get_db():
    """
    Open a new connection with the database
    """
    if 'sqlite_db' not in flask.g:
        db_filename = steven.app.config['DATABASE_FILENAME']
        flask.g.sqlite_db = sqlite3.connect(str(db_filename))
        flask.g.sqlite_db.row_factory = dict_factory
        flask.g.sqlite_db.execute("PRAGMA foreign_keys = ON")
    
    return flask.g.sqlite_db


@steven.app.teardown_appcontext
def close_db(error):
    """
    Closing the database connection at the end of a request.
    """
    assert error or not errors
    sqlite_db = flask.g.pop('sqlite_db', None)
    if sqlite_db is not None:
        sqlite_db.commit()
        sqlite_db.close()