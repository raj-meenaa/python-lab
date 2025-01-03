def read_first_n_lines(filename, n):
    with open(filename, "r") as file:
        for _ in range(n):
            print(file.readline(), end="")
read_first_n_lines("/Users/rajbahadurmeena/Desktop/College/5th Semester/Python Lab/Lab-5/lab.txt", 3)
