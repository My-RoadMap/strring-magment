# print the string in reverse order
def toString(str):
    return str[::-1]

#print odd indexes characters of the string

def oddS(str):
    for i in str:
        if str.index(i) % 2 != 0 :
            print(i, end=" - ")


#count the vowels of a string
def vowelCount(str):
    string = str.lower()
    count = 0
    for i in str:
        if (i == 'a') or (i == 'e') or (i == 'u') or (i == 'i') or (i == 'o'):
            count+=1
    return count

def letcount(str,ch):
    count=0
    for i in str:
        if ch==i:
            count+=1
    return count

#menu
def next():
    bool = input("\nDo you want to continue [y/n]?")
    if bool == 'y':
        menu()

def menu():
    str = input("Enter a string:\n#>")
    choice = int(input("=====================================MENU=================================\n"
                       "[1] - Print the string in reverse order\n"
                       "[2] - Print all the odd indexed charactes of the string\n"
                       "[3] - Print the count of all the vowels in the string\n"
                       "[4] - Print the count of the frequency of an input character in the string\nMake a choice : "))
    if choice==1:
        print(toString(str))
        next()
    elif choice == 2:
        oddS(str)
        next()
    elif choice == 3:
        print(vowelCount(str))
        next()
    elif choice==4:
        char = input("Enter the character that you want frequency :\n#>")
        print("The frequency of '{0}' in '{1}' is {2}".format(char, str, letcount(str, char)))
        next()
    else:
        print("Error! ")
        next()

menu()