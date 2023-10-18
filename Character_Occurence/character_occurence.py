string = input("Enter a string: ")

c = input("Enter a character to count its occurrences in the string: ")

x = string.count(c)

if x > 1 :
    print("The character appears",x,"times in the string.")
elif x == 1 :
    print("The character appears once in the string.")
else :
    print("The character isn't in the string.")
