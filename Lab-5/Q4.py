def count_lines(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    return len(lines)


num_lines = count_lines("/Users/rajbahadurmeena/Desktop/College/5th Semester/Python Lab/Lab-5/lab.txt")
print("Number of lines:", num_lines)
