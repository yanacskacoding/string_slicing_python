'''Write a program that asks a user to enter a string and print out it in this way. (Using Slicing)

Input:
>>> 
Enter a word: Hello
Output:
H
He
Hel
Hell
Hello

'''

#Code:

def remove_qoutes(thisString):
    return(thisString.replace("'", ""))

def remove_spaces(thisString):
    return(thisString.replace("", ""))
    
word = input("Enter the word: ")
word = remove_qoutes(word)
word = remove_spaces(word)

display = ""
for char in word:
    display += char
    print(display)