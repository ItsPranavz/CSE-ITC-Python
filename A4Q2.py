year = input("Enter a year: ")
year = int(year)

# check if the year is divisible by 4
if year % 4 == 0:
   # if the year is divisible by 4, check if it is divisible by 100
   if year % 100 == 0:
       # if the year is divisible by 100, check if it is also divisible by 400
       if year % 400 == 0:
           # if the year is divisible by 400, it is a leap year
           print(year, "is a leap year")
       else:
           # if the year is not divisible by 400, it is not a leap year
           print(year, "is not a leap year")
   else:
       # if the year is not divisible by 100, it is a leap year
       print(year, "is a leap year")
else:
   # if the year is not divisible by 4, it is not a leap year
   print(year, "is not a leap year")
