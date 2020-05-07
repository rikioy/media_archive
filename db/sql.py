import sqlite3
import os
import time
from util.log import Log
from util.path import app_path
log = Log()


class Album:
    conn = None
    album_table = 'album'

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        c = self.conn.cursor()
        c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?;", (self.album_table,))
        if c.fetchone()[0] == 1:
            pass
        else:
            log.info("create album table")
            self.create_album()
        c.close()

    def create_album(self):
        sql = '''
        CREATE TABLE album (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
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

    def insert(self, task):
        sql = '''INSERT INTO album(filename, md5, comment, media_dt, media_year, media_mon, media_day, created_at,
                updated_at) VALUES(?,?,?,?,?,?,?,?,?)'''
        created_at = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        cur = self.conn.cursor()
        task = task + (created_at, created_at)
        cur.execute(sql, task)
        self.conn.commit()
        return cur.lastrowid

    def md5_exists(self, md5):
        sql = '''SELECT * FROM album WHERE md5=?'''
        cur = self.conn.cursor()
        cur.execute(sql, md5)
        if cur.fetchone() is None:
            return False
        else:
            return True


if __name__ == "__main__":
    a = Album(os.path.join(app_path(), 'test.db'))
    id = a.insert(("a", "a", "a", "a", "a", "a", "a"))
    print(a.md5_exists('b'))
