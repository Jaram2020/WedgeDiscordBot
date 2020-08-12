import sqlite3
from pathlib import Path

DB_INSERT_SQL = 'INSERT INTO user(id) VALUES(?)'
DB_SELECT_ALL_SQL = 'SELECT * FROM user'
DB_SELECT_SQL = 'SELECT * FROM user WHERE id=?'
DB_DELETE_SQL = 'DELETE FROM user WHERE id=?'

Path("./DB").mkdir(exist_ok=True)
DB = sqlite3.connect("DB/User.db")

def Init():
    DB.execute('CREATE TABLE IF NOT EXISTS user (id TEXT PRIMARY KEY)')

def AddMember(id):
    DB.execute(DB_INSERT_SQL, (id,))
    DB.commit()

def RemoveMember(id):
    DB.execute(DB_DELETE_SQL, (id,))
    DB.commit()

def GetMembers():
    cur = DB.execute(DB_SELECT_ALL_SQL)
    rows = cur.fetchall()
    return [i[0] for i in rows]