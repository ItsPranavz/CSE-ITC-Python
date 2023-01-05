# start with the lowest possible number of pieces
pieces = 1

# keep looping until we find the correct number of pieces
while True:
   # check if the number of pieces is divisible by 5, 6, and 7
   if pieces % 5 == 2 and pieces % 6 == 3 and pieces % 7 == 2:
       # if the number of pieces is divisible by 5, 6, and 7, we have found the correct number of pieces
       break

   # if the number of pieces is not divisible by 5, 6, and 7, try the next number
   pieces += 1

   # stop if the number of pieces is greater than 200
   if pieces > 200:
       break

# print the number of pieces
print("The number of pieces is", pieces)
