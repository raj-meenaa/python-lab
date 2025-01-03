import os

def find_lines_with_nit_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, "r") as file:
                for line in file:
                    if "NIT" in line:
                        print(f"File: {filename} - Line: {line.strip()}")

# Example usage
find_lines_with_nit_in_folder("/Users/rajbahadurmeena/Desktop/College/5th Semester/Python Lab/Lab-5/lab.txt")
