from .models import Gist
import sqlite3

def search_gists(db_connection, **kwargs):
    db = sqlite3.connect('tests/populated_gists_database.db')
    db.row_factory = sqlite3.Row
    if kwargs == {}:
        cursor = db.execute('SELECT * FROM gists')
        return cursor.fetchall()
    elif kwargs.get('github_id'):
        cursor = db.execute('SELECT * FROM gists WHERE github_id = :github_id', kwargs)
        return [Gist(gist) for gist in cursor]
    elif kwargs.get('created_at'):
        cursor = db.execute('SELECT * FROM gists WHERE datetime(created_at) = datetime(:created_at)', kwargs)
        return [Gist(gist) for gist in cursor]
