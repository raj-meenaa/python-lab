import re

def find_script_tags(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if re.match(r'^<script', line.strip())]

filename = '/Users/rajbahadurmeena/Desktop/College/5th Semester/Python Lab/Lab-7/lab7.txt'
script_lines = find_script_tags(filename)

for line in script_lines:
    print(line)
