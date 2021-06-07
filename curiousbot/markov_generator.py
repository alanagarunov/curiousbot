import os
import sys
import json
import random


def readArguments(nameofperson):
    nameoffile = "dictionary" + nameofperson + ".json"
    # ask = int(input("How long do you want your sentence to be? "))
    length = 100
    filename = nameoffile

    # numArguments = len(sys.argv) - 1

    """
	if numArguments >= 1:
		length = int(sys.argv[1])
	if numArguments >= 2:
		filename = sys.argv[2]
	"""

    return length, filename


def loadDictionary(filename):
    if not os.path.exists(filename):
        sys.exit("Error: No directory")

    file = open(filename, "r")
    dictionary = json.load(file)
    file.close()
    return dictionary


def pickRandom(dict):
    randNum = random.randint(0, len(dict) - 1)
    newWord = list(dict.keys())[randNum]
    return newWord


def getNextWord(word, dict):
    if word not in dict:
        newWord = pickRandom(dict)
        return newWord
    # here is where it choses the word, picks the word that occurs the most
    else:
        canadiates = dict[word]
        canadiatesNormal = []
        for word in canadiates:
            freq = canadiates[word]
            for i in range(0, freq):
                canadiatesNormal.append(word)

        rnd = random.randint(0, len(canadiatesNormal) - 1)
        return canadiatesNormal[rnd]


def maingenerator(name):
    length, filename = readArguments(name)
    dictionary = loadDictionary(filename)

    lastWord = "dust"
    result = ""
    for i in range(0, length):
        newWord = getNextWord(lastWord, dictionary)
        result = result + " " + newWord
        lastWord = newWord
    # print(result)
    return result


# maingenerator()
