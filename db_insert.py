import sqlite3
import os
import hindi_stemmer
def check_for_db():
    if not os.path.exists("words.db"):
        conn = sqlite3.connect("words.db")
        create_table = "CREATE TABLE words  (Word TEXT NOT NULL PRIMARY KEY,  Stemmed  TEXT NOT NULL)"
        conn.execute(create_table)
        conn.commit()
def search(word):
        check_for_db()
        conn = sqlite3.connect("words.db")
        cursor = conn.cursor()
        test = "'"+word+"'"
        search_table = "select word FROM words WHERE word="+test
        cursor.execute(search_table)
        x = cursor.fetchall()
        if(len(x)!=0):
                print("Word Found In The Database:",x)
        else:
                x = hindi_stemmer.hi_stem(word)
                insert_text = "INSERT INTO words (word,stemmed) VALUES (\'%s\', \'%s\')" % (word, x)
                cursor.execute(insert_text)
                conn.commit()
                print("word not found in the database:", x, " word inserted into the database")
if __name__ == "__main__":
        f = open("dataset.txt",'r', encoding = 'utf-8')
        while True:
                x = f.readline()
                if(x == None):
                        break
                for word in x.split():
                        search(word)