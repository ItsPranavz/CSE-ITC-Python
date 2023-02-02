str1=input("Enter the hyphen-separated sequence of words\n")      #taking the input string
list1=str1.split('-')                                           #extracting the words into a list
list1=sorted(list1)                                             #sorting the words
str1='-'.join(list1)                                            #converting sorted words back to hyphen separated string
print(str1)                                                     #printing the desired string
