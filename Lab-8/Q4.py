import sqlite3
def connect_db():
    conn = sqlite3.connect('student.db')
    return conn
def delete_record():
    conn = connect_db()
    cursor = conn.cursor()
    s_no = int(input("Enter Serial Number of the record to delete: "))
    cursor.execute("DELETE FROM students WHERE S_No = ?", (s_no,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"Record with Serial Number {s_no} deleted successfully.")
    else:
        print(f"No record found with Serial Number {s_no}.")
    
    conn.close()
if __name__ == "__main__":
    delete_record()
