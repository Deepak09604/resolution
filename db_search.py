import sqlite3
import os
import hindi_stemmer
def check_for_db():
    if not os.path.exists("words.db"):
        conn = sqlite3.connect("words.db")
        create_table = "CREATE TABLE words (word TEXT NOT NULL PRIMARY KEY,  stemmed TEXT NOT NULL)"
        conn.execute(create_table)
        conn.commit()
def search(word):
        check_for_db()
        conn = sqlite3.connect("words.db")
        cursor = conn.cursor()
        test = "'"+word+"'" 
        search_table = "select * FROM words WHERE word="+test
        cursor.execute(search_table)
        x = cursor.fetchall()
        if(len(x)!=0):
                print("word found in the database:",x)
        else:
                x = hindi_stemmer.hi_stem(word)
                insert_text = "INSERT INTO words (word,stemmed) VALUES (\'%s\', \'%s\')" % (word, x)
                cursor.execute(insert_text)
                conn.commit()
                print("word not found in the database:", x, "inserted into the database")