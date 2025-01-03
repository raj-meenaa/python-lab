import sqlite3
def connect_db():
    conn = sqlite3.connect('student.db')
    return conn
def list_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall() 
    print("Tables in the database:")
    for table in tables:
        print(table[0])
    conn.close()
if __name__ == "__main__":
    list_tables()
