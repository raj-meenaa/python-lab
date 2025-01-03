import os

def find_files_with_nit_in_subdirs(folder_path):
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".txt"):
                file_path = os.path.join(root, filename)
                with open(file_path, "r") as file:
                    if "NIT" in file.read():
                        print(f"File with 'NIT': {file_path}")

# Example usage
find_files_with_nit_in_subdirs("Lab-5")
