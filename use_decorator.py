import logging
import sqlite3
from contextlib import contextmanager

@contextmanager
def open_db(file_name):
    connection = sqlite3.connect(file_name)
    try:
        cursor = connection.cursor()
        yield cursor
    finally:
        connection.commit()
        connection.close()