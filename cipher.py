#/usr/bin/python3
from random import randrange
import time
import ast

keyMapperFile = ""


def main():
    print("=== Welcome to python cipher v0.1.0 ===")
    userInput = ""
    while(True):
        userInput = input("Choose a option\n0 Specify an existing cipher key mapping to use\n1 Generate a cipher key\n2 Encrypt some input or text file \n3 Decrypt some input or a text file\n4 Help and Instructions\n\n")
        if userInput == "q":
            break
        if userInput == "1":
            userInput = input("Enter a filename (.txt) for the generated key to save to,\ninclude filepath info if applicable\n\n")
            generateKey(userInput)


def generateKey(newFile):
    #associate letters of alphabet with a random character and save mapped characters to text file
    print("Generating new key mapping...")
    time.sleep(1.5)
    charsToTranslate = ["a","b","c","d", "e", "f" , "g", "h","i","j","k","l","m","n","o","p","q","r","s","t","u",
    "v","w","x","y","z"," "]
    charsToChoose = ["a", "b", "c" , "d", "A" , "B" , "C" , "E", "Z", "x" , "O","o", "1", "!", "2", "@", "3", "#", 
    "4", "$", "5","&", "9" , "^", "/", "y", "v"]
    chosenIndex = 0 
    keyMap = {}
    for i in range(0,len(charsToTranslate)):
        currentChar = charsToTranslate[i]
        chosenIndex = randrange(len(charsToChoose))
        currentTranslate = charsToChoose[chosenIndex]
        charsToChoose.pop(chosenIndex)
        keyMap[currentChar] = currentTranslate
    print("Saving key map to " + newFile+"...")
    time.sleep(1)
    saveFile = open(newFile,"w")
    saveFile.write(str(keyMap))
    saveFile.close()
    print("Done\n")
    time.sleep(2)


def encrypt(toTranslate):
    #replace real string values with associated key values
    key = open(r"cipherKey/keyMap.txt","r")  #!!!!
    encryptedString = ""
    for i in range(0,len(toTranslate)):
        currentLetter = toTranslate[i]
        currentLine = str(key.readlines())
        encryptedLetter = currentLine[1]
        encryptedString = encryptedString + encryptedLetter

    print("Encrypted string: " + encryptedString)
    key.close()
    return encryptedString


def decrypt(toDecrypt,keyMap):
    key = open(r"cipherKey/keyMap.txt", "r")
    decryptedString = ""
    for i in range(0,len(toDecrypt)):
        for i in key.readlines():
            currentLine = key.readlines()
            realLetter = currentLine[0]
            encryptedLetter = currentLine[1]
            if(toDecrypt == encryptedLetter):
                decryptedString = decryptedString + decryptedString
    print("Decrypted String is: " + decryptedString)


def setKeyMapper(filename):
    global keyMapperFile
    keyMapperFile = filename

main()
'''
with open('exampleKeyMap.txt') as f:
    data = f.read()
print("data type before process: ", type(data))
d = ast.literal_eval(data)
print("data type after: ", type(d))
'''