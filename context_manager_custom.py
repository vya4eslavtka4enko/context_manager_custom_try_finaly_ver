import logging
import sqlite3

class SQLite:
    def __init__(self,file_name:str):
        self.file_name = file_name
        self.connection = sqlite3.connect(self.file_name)
    def __enter__(self):
        logging.info("Calling __enter__")
        return.self.connection.cursor()
    def __exit(self)
        logging.info("Calling __exit__")
        self.connection.commit()
        self.connection.close()
        

#def main():
 #   loggin.basicConfig(level=loggin.INFO)
#     connection = sqlite3.connect('Thi is database.db')
  #  try:
   #     cursor = connection.cursor()
    #    cursor.execute('SELECT * FROM **')
     #   logging.info(cursor.fetchall())
    #finally:
     #   logging.info('Closing connection')
      #  connection.close()
        
        
def main():
    logging.basicConfig(level=logging.INFO)
    with SQLite(file_name="database.db") as cursor:
        cursor.execute("SELECT * FROM **")
        logging.info(cursor.fetchall())
        
if __name__ == "__main__":
    main()