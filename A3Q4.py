# Program to print performance from grade points
grade_point=int(input("Enter grade points : "))
g1={10:"Your grade is 'A+' and Outstanding performance.",
     9:"Your grade is 'A' and Excellent performance.",
     8:"Your grade is 'B+' and Very Good performance.",
     7:"Your grade is 'B' and Good performance.",
     6:"Your grade is 'C+' and Average performance.",
     5:"Your grade is 'C' and Below Average performance.",
     4:"Your grade is 'D' and Poor performance."}
# Applying Conditions for correct grade range
if 4<=grade_point<=10:
        statement=g1.get(grade_point)
        print(statement)
else:
       print("\nError\nPlease enter grade in range [4,10]")
