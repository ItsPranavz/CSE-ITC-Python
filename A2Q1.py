# Defining String Input
string = "Python is a case sensitive language"
# Finding length of input string
length = len(string)
print("1)", str(length) + "\n")
# Reversing order of string
reverse_string = string[::-1]
print("2)", reverse_string+"\n")
# Using string slicing
sliced_string = string[12:-9]
print("3)", sliced_string+"\n")
# Replacing substring
print("4)", string[:12]+" object oriented "+string[-8:]+"\n")
# Searching for substring
print("5)",string.find("a"))
# Removing all whitespaces
print("\n6)",string.replace(" ","")+"\n")