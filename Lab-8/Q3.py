import sqlite3
def connect_db():
    conn = sqlite3.connect('student.db')
    return conn
def count_records():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()[0]
    print(f"Total number of records in the 'students' table: {count}")
    conn.close()
if __name__ == "__main__":
    count_records()
