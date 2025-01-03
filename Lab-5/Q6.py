def largest_word_in_each_line(filename):
    with open(filename, "r") as file:
        for line in file:
            words = line.split()
            if words:
                largest_word = max(words, key=len)
                print(f"Largest word in line: '{largest_word}'")

# Example usage
largest_word_in_each_line("/Users/rajbahadurmeena/Desktop/College/5th Semester/Python Lab/Lab-5/lab.txt")
