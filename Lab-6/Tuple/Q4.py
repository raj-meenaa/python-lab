sample_tuple = (1, 2, 3, 4)
modified_tuple = tuple(x for x in sample_tuple if x != 2)  # Removing '2'
print(modified_tuple)
