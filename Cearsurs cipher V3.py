#imports
import time
import string #FOR list use
import random
#from mitchpy import *
#globals
global finalout
global x
global out
#Custom commands
"""
mitchpy now does this
"""
def sleep(num):
    time.sleep(num)

def blankspace(num):
    while num > 0:
        print()
        num -= 1

#vars
devtool = 0
ver = "3.0.0"
x = 4
out = ""
finalout = ""
letters = list(string.ascii_uppercase)
letters_upper = list(string.ascii_uppercase)
letters_lower = list(string.ascii_lowercase)
#letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#funt

def selection():
    global sent
    global offset
    global x
    print()
    print()
    print()
    print("What Is the Sentence You want to Process?")
    print()
    sent = input() #SENTNECE INPUT
    print("Your sentence is '", sent,"'")
    print()
    sleep(1)
    print()
    print("What is the offset? ")
    print("(-26 to 26)")
    x = 4
    while x == 4: #ERROR CHECKING
        offset = int(input(":  ")) #OFFSET INPUT
        if offset > 26 or offset < -26:
            print("Error Please input a number beween -26 to 26!")
        else:
            break
    x = 4
    print()
    print("Your Offset is", offset)
    print()
    time.sleep(1)


"""
i is the current letter being encrypted. in the veriable "sent"
letters is the array of letters
.index(i) finds the number what the letter is in the list
+ offset adds the offset to that number

"""
def encrp():
    finalout = ""
    for i in sent: #Loop for Encrypting
        if i == " ":
            finalout = finalout + " "
        elif i == ".":
            finalout = finalout + "."
        elif i == ",":
            finalout += ","
        elif i == "1":
            finalout += "1"
        elif i == "2":
            finalout += "2"
        elif i == "4":
            finalout += "4"
        elif i == "3":
            finalout += "3"
        elif i == "5":
            finalout += "5"
        elif i == "0":
            finalout += "0"
        elif i == "6":
            finalout += "6"
        elif i == "7":
            finalout += "7"
        elif i == "8":
            finalout += "8"
        elif i == "9":
            finalout += "9"
        elif i == "!":
            finalout += "!"
        else:
            #Code is the same for each option but they both eycript against a lower and upper case letters array, rather than just encoding against one uppercase one
            if i == i.upper(): #If it is a upper case letter
                out = letters_upper.index(i)+offset
                if out >= 26:
                    out -= 26
                elif out < 0:
                    out += 26
                finalout = finalout + letters_upper[out]
                out = letters_upper.index(i)+offset

            elif i == i.lower(): #If it is a lower case letter
                out = letters_lower.index(i)+offset
                if out >= 26:
                    out -= 26
                elif out < 0:
                    out += 26
                finalout = finalout + letters_lower[out]
                out = letters_lower.index(i)+offset

            if devtool == 1:
                print(letters.index(i)+offset)

    print("The sentence is: ")
    print(finalout)


def decrp():
    finalout = ""
    x = 5
    for i in sent: #loop for decrypting
        if i == " ": # if system for non letter inputs
            finalout = finalout + " "
        elif i == ".":
            finalout = finalout + "."
        elif i == "!":
            finalout += "!"
        elif i == ",":
            finalout += ","
        elif i == "1":
            finalout += "1"
        elif i == "2":
            finalout += "2"
        elif i == "4":
            finalout += "4"
        elif i == "3":
            finalout += "3"
        elif i == "5":
            finalout += "5"
        elif i == "0":
            finalout += "0"
        elif i == "6":
            finalout += "6"
        elif i == "7":
            finalout += "7"
        elif i == "8":
            finalout += "8"
        elif i == "9":
            finalout += "9"
        else: #Ofter wise
            if i == i.upper():
                out = letters_upper.index(i)-offset
                if out >= 26:
                    out -= 26
                elif out < 0:
                    out += 26
                finalout = finalout + letters_upper[out]
                out = letters_upper.index(i)-offset

            elif i == i.lower():
                out = letters_lower.index(i)-offset
                if out >= 26:
                    out -= 26
                elif out < 0:
                    out += 26
                finalout = finalout + letters_lower[out]
                out = letters_lower.index(i)-offset
    print(finalout)
    print()
    print()

def brutedecrp():
    print("What Is the Sentence You want to brute force?")
    print()
    sent = input().upper() #SENTNECE INPUT
    print("Your sentence is '", sent,"'")
    loop55 = 1
    counter = 0
    while loop55 == 1:
        counter += 1
        if counter >= 27:
            break
        currentoffset = counter
        finalout = ""
        for i in sent: #loop for decrypting
            if i == " ": # if system for non letter inputs
                finalout = finalout + " "
            elif i == ".":
                finalout = finalout + "."
            elif i == "!":
                finalout += "!"
            elif i == ",":
                finalout += ","
            elif i == "1":
                finalout += "1"
            elif i == "2":
                finalout += "2"
            elif i == "4":
                finalout += "4"
            elif i == "3":
                finalout += "3"
            elif i == "5":
                finalout += "5"
            elif i == "0":
                finalout += "0"
            elif i == "6":
                finalout += "6"
            elif i == "7":
                finalout += "7"
            elif i == "8":
                finalout += "8"
            elif i == "9":
                finalout += "9"
            else: #Ofter wise
                if i == i.upper():
                    out = letters_upper.index(i)-currentoffset
                    if out >= 26:
                        out -= 26
                    elif out < 0:
                        out += 26
                    finalout = finalout + letters_upper[out]
                    out = letters_upper.index(i)-currentoffset

                elif i == i.lower():
                    out = letters_lower.index(i)-currentoffset
                    if out >= 26:
                        out -= 26
                    elif out < 0:
                        out += 26
                    finalout = finalout + letters_lower[out]
                    out = letters_lower.index(i)-currentoffset
        print(counter, "=", finalout)


#main code

#Intro
blankspace(2)
print("Caesar cipher ting")
while x == 4: #Start loop for menu
    print()
    print("ENTER E to Encrypt")
    print("ENTER D to Decrypt")
    print("ENTER B to Brute Force Decrypt")
    print("ENTER Q to Quit!")
    print()
    type = input()
    type = type.upper()
    if type == "E" or type == "ENCRYPT": #if input = e encrypt
        selection()
        sent = list(sent)
        encrp()
    elif type == "D" or type == "DECRYPT": # if input d decrypt
        selection()
        sent = list(sent)
        decrp()
    elif type == "B" or type == "BRUTEDECRYPT": # if input b brutedecrypt
        brutedecrp()
    elif type == "Q" or type == "QUIT": #If input q quit
        print("Goodbye!")
        break
    elif type == "T" or type == "DEV":
        devtool = 1
        print("Devtools activated")
        continue
    else: #If invaild input
        print("INVAILD INPUT!!")
        blankspace(2)
        continue




