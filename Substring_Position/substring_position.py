string = input("Enter a string: ")

c = input("Enter the substring you want to find in the string: ")

x = string.find(c)

if x != -1:
    print("The first occurrence of '"+c+"' in the string is at position", x)
else:
    print("The substring is not found in the string.")
