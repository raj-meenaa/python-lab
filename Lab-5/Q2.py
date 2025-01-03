
def file_operations_demo(file_path):
    
    with open(file_path, 'w') as file:
        file.write("Hello, this is a demonstration of file handling.\n")
        file.write("Using seek(), tell(), and checking if the file is closed.\n")

    
    with open(file_path, 'r') as file:
        
        content = file.read()
        print("File content after writing:")
        print(content)

        
        file.seek(0)
        print("\nAfter seek(0), we move back to the start and read the first line:")
        print(file.readline())

        
        position = file.tell()
        print(f"\nCurrent position after reading the first line: {position}")

        
        file.seek(10)
        print(f"\nAfter seek(10), the file pointer moves to position 10 and reads from there:")
        print(file.readline())

    
    if file.closed:
        print("\nThe file is closed now.")


file_path = '/Users/rajbahadurmeena/Desktop/College/5th Semester/Python Lab/Lab-5/lab.txt'


file_operations_demo(file_path)
