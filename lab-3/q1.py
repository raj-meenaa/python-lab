def binary_decimal(binary):
    decimal = 0
    binary = str(binary)
    length = len(binary)
    for i in range(length):
        decimal+= int(binary[length-i-1])*(2**i)

    return decimal

binary_input = input("Enter a binary number: ")
decimal_output = binary_decimal(binary_input)
print(decimal_output)
