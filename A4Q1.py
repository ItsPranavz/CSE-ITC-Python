# Program to output a grade
# Prompt the user to enter their marks
marks = int(input("Enter your marks: "))

# Determine the corresponding grade based on the rules provided
if marks < 25: # Marks below 25
    grade = "F"
elif marks >= 25 and marks < 45: # Marks between 25 and 45
    grade = "E"
elif marks >= 45 and marks < 50: # Marks between 45 and 50
    grade = "D"
elif marks >= 50 and marks < 60: # Marks between 50 and 60
    grade = "C"
elif marks >= 60 and marks < 80: # Marks between 60 and 80
    grade = "B"
else: # Marks above 80
    grade = "A"

# Print out the grade
print("Your grade is:", grade)
