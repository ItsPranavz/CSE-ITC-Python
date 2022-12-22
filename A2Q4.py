# Getting input from the user
num_1 = int(input("Please enter first number : "))
num_2 = int(input("Please enter second number : "))
num_3 = int(input("Please enter third number : "))
# Comparing first two numbers
if num_1>num_2:
    # Comparing greater number one with last number
    if num_1>num_3:
        print(f"The greatest number is {num_1}")
    else:
        print(f"The greatest number is {num_3}")
else:
    # Comparing greater number two with last number
    if num_2>num_3:
        print(f"The greatest number is {num_2}")
    else:
        print(f"The greatest number is {num_3}")