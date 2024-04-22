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
        
        
def main():
    logging.basicConfig(level=logging.INFO)
    with open_db(file_name="database.db") as cursor:
        cursor.execute("SELECT * FROM **")
        logging.info(cursor.fetchall())
        
if __name__ == "__main__":
    main()