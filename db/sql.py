import sqlite3
import logging


class Sql:
    conn = None
    album_table = 'album'

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        c = self.conn.cursor()
        c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?;", (self.album_table,))
        if c.fetchone()[0]==1 :
            logging.debug("table exists.")
            print("a")
        else:
            logging.info("not table")
            self.create_album()
            print("b")
        c.close()


    def create_album(self):
        sql = '''
        CREATE TABLE album (
            id int PRIMARY KEY NOT NULL,
            filename TEXT NOT NULL,
            md5 TEXT NOT NULL,
            comment TEXT,
            media_dt DATETIME,
            media_year int,
            media_mon int,
            media_day int,
            created_at DATETIME,
            updated_at DATETIME 
        );
        '''
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        cur.close


    def insert(self):
        print('insert record')

    def check(self):
        print('check exists')


if __name__ == "__main__":
    db = Sql('d:/test.db')
