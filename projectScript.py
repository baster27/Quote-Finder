from random import choice
from string import ascii_lowercase as letters

listOfDomains = ['myexample.com','yourexample.com','example.com']

quotes = [  "There is nothing to fear but fear itself.",
            "Ever danced with the devil in the pale moonlight?",
            "Throw me to the wolves and I will come back leading the pack.",
            "Home is where your horse is."]

def generateName(lengthOfName):
    return ''.join(choice(letters) for i in range(lengthOfName))

def getDomain(listOfDomains):
    return choice(listOfDomains)

def getQuotes(listOfQuotes):
    return choice(listOfQuotes)

def generateRecords(lengthOfName, listOfDomains, totalRecords, listOfQuotes):
    with open("data.txt", "w") as toWrite:
        for num in range(totalRecords):
            key = generateName(lengthOfName)+'@'+getDomain(listOfDomains)
            value = getQuotes(quotes)
            toWrite.write(key + ': ' + value + '\n')
        toWrite.write("brian@gmail.com: Don't let me leave Murph\n")
        toWrite.write("example@example.com: All I do is win")

generateRecords(10, listOfDomains, 100000, quotes)
