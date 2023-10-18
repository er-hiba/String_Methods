string = input("Enter a string: ")

x = len(string)

if x > 1 :
    print("This string has", x ,"characters.")
elif x == 1 :
    print("This string has one character.")
elif x == 0 :
    print("This string is empty.")
