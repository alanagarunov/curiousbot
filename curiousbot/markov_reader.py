import sys
import json
import os

# get arguments
def readArguments(nameofperson):
    nameoffile = "dictionary" + nameofperson + ".json"
    # numArguments = len(sys.argv) - 1
    dictionaryFile = nameoffile
    inputFile = ""

    """
	if numArguments >= 1:
		dictionaryFile = sys.argv[1]
	if numArguments >= 2:
		dictionaryFile = sys.argv[2]
	"""

    return dictionaryFile, inputFile


# create json file for the first time or open it
def loadDictionary(filename):
    if not os.path.exists(filename):
        file = open(filename, "w")
        json.dump({}, file)
        file.close()

    file = open(filename, "r")
    dictionary = json.load(file)
    file.close()
    return dictionary


# appends to dictionary
def learn(dict, input):
    splitword = input.split(" ")
    for i in range(0, len(splitword) - 1):
        currentWord = splitword[i]
        nextWord = splitword[i + 1]

        # add word
        if currentWord not in dict:
            dict[currentWord] = {nextWord: 1}
        else:
            allNextWords = dict[currentWord]
            if nextWord not in allNextWords:
                dict[currentWord][nextWord] = 1
            else:
                # increase frequency of word
                dict[currentWord][nextWord] = dict[currentWord][nextWord] + 1
    return dict


def updateFile(filename, dictionary):
    file = open(filename, "w")
    json.dump(dictionary, file)
    file.close()


def mainadder(message, name):
    dictionaryFile, inputFile = readArguments(name)
    dictionary = loadDictionary(dictionaryFile)

    if inputFile == "":
        userInput = message
        if userInput == "":
            print("No input")
        dictionary = learn(dictionary, userInput)
        updateFile(dictionaryFile, dictionary)
    else:
        print("Wha")


# mainadder()
