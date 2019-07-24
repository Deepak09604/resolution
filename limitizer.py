import sqlite3
import os
def check_for_db():
    if not os.path.exists("exception.db"):
        conn = sqlite3.connect("exception.db")
        create_table = "CREATE TABLE words (word TEXT NOT NULL PRIMARY KEY,  stemmed TEXT NOT NULL)"
        conn.execute(create_table)
        conn.commit()
def search(word):
        check_for_db()
        conn = sqlite3.connect("exception.db")
        cursor = conn.cursor()
        test = "'"+word+"'" 
        search_table = "select * FROM words WHERE word="+test
        cursor.execute(search_table)
        x = cursor.fetchall()
        if(len(x)!=0):
            print("Exception found:",x)
            return 1
        else:
            return 0