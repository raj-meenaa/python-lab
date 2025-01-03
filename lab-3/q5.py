def float_to_binary(number, precision=10):
    integer_part = int(number)
    fractional_part = number - integer_part
    integer_binary = bin(integer_part).replace("0b", "")

    fractional_binary = ""
    while precision > 0:
        fractional_part *= 2
        bit = int(fractional_part)
        fractional_binary += str(bit)
        fractional_part -= bit
        precision -= 1

   
    binary_representation = integer_binary + "." + fractional_binary
    return binary_representation


user_input = float(input("Enter a floating-point number: "))

binary_output = float_to_binary(user_input)
print(f"Binary equivalent of {user_input} is: {binary_output}")