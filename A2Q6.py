# Program to determine existence of triangle with sides given
# Taking user input for sides of triangle
side_1 = int(input("Please enter length of first side : "))
side_2 = int(input("Please enter length of second side : "))
side_3 = int(input("Please enter length of third side : "))
# Finding all possible permutations of two side sums
s1_s2 = side_1 + side_2
s2_s3 = side_2 + side_3
s3_s1 = side_3 + side_1
# Comparing sum of two sides with the third using if statement
if s1_s2 <= side_3 or s2_s3 <= side_1 or s3_s1 <= side_2:
    # The triangle cannot be formed
    print("No, Given lengths don't form triangle.")
else:
    # The triangle can be formed
    print("Yes, Given lengths form a triangle.")
