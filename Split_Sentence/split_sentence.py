string = input("Enter a sentence: ")

string = string.strip()

if string == "" :
    print("The input is empty.")

else:
    x = string.split()
    print("The words in the sentence are:",x)
