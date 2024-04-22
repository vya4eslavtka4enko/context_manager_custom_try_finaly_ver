import sqlite3

def main():
    loggin.basicConfig(level=loggin.INFO)
    connection = sqlite3.connect('Thi is database.db')
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM **')
        logging.info(cursor.fetchall())
    finally:
        logging.info('Closing connection')
        connection.close()