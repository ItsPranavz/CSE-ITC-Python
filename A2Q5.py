# Program to check substring "name"
# Taking inpur from the user
string = input("Please enter a sentence : ")
# Printing the label for the process
print("Checking for \"name\" in your sentence.")
# Checking for substring in input
if "name" in string:
    # When the string contains substring
    print("Yes, substring name is present.")
else:
    # When the string does not contain substring
    print("No, substring name is absent.")
