# ref: https://www.datacamp.com/tutorial/tutorial-postgresql-python
# Used to interact with database

import psycopg2
import os


POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "ph-gen-app-database")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", "5432")
POSTGRES_DATABASE = os.environ.get("POSTGRES_DATABASE", "ph-gen-db")
POSTGRES_USER = os.environ.get("POSTGRES_USER", "app")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "123")


def create_connection():
    conn = psycopg2.connect(
        database = POSTGRES_DATABASE, 
        user = POSTGRES_USER, 
        host= POSTGRES_HOST,
        password = POSTGRES_PASSWORD,
        port = POSTGRES_PORT
    )
    return conn


def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS phrases (
            id     SERIAL,
            phrase TEXT PRIMARY KEY
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()


def add_phrase(phrase):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO phrases (Phrase) VALUES ('{phrase}')")
    
    conn.commit()
    cursor.close()
    conn.close()


def get_phrase_by_id(id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM phrases WHERE id = {id}")
    
    # item format: (ID, PHRASE)
    item = cursor.fetchone()
    
    conn.commit()
    cursor.close()
    conn.close()

    return item[1]


def get_random_phrase():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM phrases ORDER BY RANDOM() LIMIT 1")
    
    # item format: (ID, PHRASE)
    item = cursor.fetchone()
    
    conn.commit()
    cursor.close()
    conn.close()

    return item[1] 


if __name__ == "__main__":
    create_table()
    add_phrase("Hello db 1!")
    add_phrase("Hello db 2!")
    add_phrase("Hello db 3!")
    add_phrase("Hello db 4!")
    print(get_random_phrase())
