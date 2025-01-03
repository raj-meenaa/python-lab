
filename='/Users/rajbahadurmeena/Desktop/College/5th Semester/Python Lab/Lab-5/lab.txt'
with open(filename, 'r') as file:
    lines=file.readlines()
nit_lines=[line for line in lines if line.startswith('NIT')]

for line in nit_lines:
     print(line.strip())