#/usr/bin/python3
from random import randrange
import time
import ast

keyMapperFile = "exampleKeyMap.txt"


def main():
    print("=== Welcome to python cipher v0.1.0 ===")
    userInput = ""
    while(True):
        userInput = input("Choose a option (or q to exit):\n0 Specify an existing cipher key mapping to use\n1 Generate a cipher key\n2 Encrypt some input or text file \n3 Decrypt some input or a text file\n4 Help and Instructions\n\n")
        if userInput == "q":
            break
        if userInput == "0":
            filename = input("Enter filename (.txt) to use an existing key mapping\n")
            setKeyMapper(filename)
        if userInput == "1":
            userInput = input("Enter a filename for the generated key to save to,\ninclude filepath info if applicable\n\n")
            generateKey(userInput)
        if userInput == "2":
            userInput = input("Enter some text to encrypt: \n\n")
            encrypt(userInput)


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
    print("Saving key map to " + newFile+".txt...")
    time.sleep(1)
    saveFile = open(newFile+".txt","w")
    saveFile.write(str(keyMap))
    saveFile.close()
    print("Done\n")
    time.sleep(2)


def encrypt(toTranslate):
    #replace real string values with associated key values
    global keyMapperFile
    print("Getting key map from " + keyMapperFile+"...")
    time.sleep(0.8)
    with open(keyMapperFile) as f:
        data = f.read()
    keyDict = ast.literal_eval(data)
    encryptedString = ""
    currentEncryptChar = ""
    print("Encrypting...")
    time.sleep(1.2)
    for i in range(0,len(toTranslate)):
        currentEncryptChar = keyDict[toTranslate[i]]
        encryptedString = encryptedString + currentEncryptChar
    print("Done")
    time.sleep(0.5)
    print("Encrypted string is below\n")    
    print(encryptedString+"\n\n")
    time.sleep(2)

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
