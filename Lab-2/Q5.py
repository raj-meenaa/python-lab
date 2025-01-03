def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
n=int(input("Enter the value of n: "))
print(f"The Factorial of {n} is: {factorial(n)}")