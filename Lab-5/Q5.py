def count_chars_and_words(filename):
    with open(filename, "r") as file:
        text = file.read()
        num_chars = len(text)
        num_words = len(text.split())
    return num_chars, num_words


chars, words = count_chars_and_words("/Users/rajbahadurmeena/Desktop/College/5th Semester/Python Lab/Lab-5/lab.txt")
print(f"Characters: {chars}, Words: {words}")
