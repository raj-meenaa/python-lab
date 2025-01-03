def binary_decimal(binary):
    decimal = 0
    binary = str(binary)
    length = len(binary)
    for i in range(length):
        decimal+= int(binary[length-i-1])*(2**i)

    return decimal
def binary_decimal_recurrsive(binary):
    if binary=="":
        return 0
    return int(binary[0])*(2**(len(binary)-1)) + binary_decimal_recurrsive(binary[1:])


binary_input = input("Enter a binary number: ")
decimal_output = binary_decimal_recurrsive(binary_input)
print(decimal_output)
