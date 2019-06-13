# PEP 572

# Use in comprehensions
print([squared for n in range(100) if (squared := n * n) % 2 == 1])  # get odd squares
print(squared)


# Use in if statements
array = [1, 2, 3, 4]
if (length := len(array)) > 3:
    print(f"Length is {length}")


# Use in the same conditional statement
dictionary = {1: '1', 2: '2'}
if (value := dictionary.get(1)) and value == '1':
    print(value)



# Use in while statements
values = [1, 2, 3, 4]
while (val := values.pop(0)) < 3:
    print(val)


# DON'T DO THIS
val4 = (val3 := (val2 := (val1 := 2) * 2) * 2) * 2
print(f"{val1 = }, {val2 = }, {val3 = }, {val4 = }")
