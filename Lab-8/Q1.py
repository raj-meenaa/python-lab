import sqlite3
import os
def connect_db():
    conn = sqlite3.connect('student.db')
    return conn
def addTable():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        S_No INTEGER PRIMARY KEY,
                        SName TEXT NOT NULL,
                        Contact_No INTEGER
                     )''')
    conn.commit()
    conn.close()
def addRecords():
    conn = connect_db()
    cursor = conn.cursor()
    s_no = int(input("Enter Serial Number: "))
    s_name = input("Enter Student Name: ")
    contact_no = int(input("Enter Contact Number: "))
    cursor.execute("INSERT INTO students (S_No, SName, Contact_No) VALUES (?, ?, ?)",
                   (s_no, s_name, contact_no))
    conn.commit()
    conn.close()
    print("Record added successfully.")
def ViewRecords():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    for record in records:
        print(record)
    conn.close()
def UpdateRecord():
    conn = connect_db()
    cursor = conn.cursor()
    s_no = int(input("Enter Serial Number of the record to update: "))
    new_name = input("Enter the new name: ")
    new_contact = int(input("Enter the new contact number: "))
    cursor.execute("UPDATE students SET SName = ?, Contact_No = ? WHERE S_No = ?",
                  (new_name, new_contact, s_no))
    conn.commit()
    conn.close()
    print("Record updated successfully.")
def list_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        print(table[0])
    conn.close()
def count_records():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()[0]
    print(f"Total records: {count}")
    conn.close()
def delete_record():
    conn = connect_db()
    cursor = conn.cursor()
    s_no = int(input("Enter Serial Number of the record to delete: "))
    cursor.execute("DELETE FROM students WHERE S_No = ?", (s_no,))
    conn.commit()
    conn.close()
    print("Record deleted successfully.")
def main_menu():
    addTable()
    while True:
        print("\nMain Menu:")
        print("1. Add a record")
        print("2. View all records")
        print("3. Update a record")
        print("4. List all tables")
        print("5. Count total records")
        print("6. Delete a record")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            addRecords()
        elif choice == '2':
            ViewRecords()
        elif choice == '3':
            UpdateRecord()
        elif choice == '4':
            list_tables()
        elif choice == '5':
            count_records()
        elif choice == '6':
            delete_record()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main_menu()
