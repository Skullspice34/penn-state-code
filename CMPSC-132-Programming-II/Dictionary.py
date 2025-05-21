listOfWords = ["hola", "como", "tu", "carro", "es", "feo"]

myDict = {}

for word in listOfWords:
    wordLen = len(word)
    sameCnt = 0

    if wordLen not in myDict:#check if the value isn't already added to the dictionary
        for word2 in listOfWords:#count the number of occurances for the same length
            if wordLen == len(word2):
                sameCnt += 1

        myDict[wordLen] = sameCnt #add cvalues to dictionary

print(myDict)