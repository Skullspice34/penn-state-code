# Lab #1

##Is Valid##

chartwosix = []

def isValid(txt):
    if txt.isalpha() and len(txt) == 26: #checks if its only letters and it has 26 characters
        for l in range(0, 24): 
            if txt[l].lower() in txt[l + 1 :25].lower(): # checks for repeated letters
                return False
            
        return True      
    else:
        return False  

##Words## 

def get_words(filename):
    word = open(filename, "r")#opens file
    #reads the file
    word.close
    strp = rd.strip()#eliminates spaces in the first posision and last
    rpl = strp.replace( "\n"," ")#replaces enters with spaces
    splt = rpl.split(" ")#creates an array 
    return list(filter(None, splt))#to remove empty strings caused by double spaces

##Histogram##

listOfWords = ['hello', 'there', 'spring', 'is', 'here']#write words HERE

def get_histogram(words):
    myDict = {}

    for word in words:
        wordLen = len(word)
        sameCnt = 0

        if wordLen not in myDict:#check if the value isn't already added to the dictionary
            for word2 in words:#count the number of occurances for the same length
                if wordLen == len(word2):
                    sameCnt += 1

            myDict[wordLen] = sameCnt #add cvalues to dictionary

    print(myDict)

##Punctuation##

strInfo = "I like chocolate cake!!(!! It's the best flavor..;.$ for real"

def removePunctuation(aString):

    myDict = {}

    for i in range(len(aString)):
        
        if not aString[i].isalpha() and aString[i] != " ":
            sameCnt = 0
            strLetter = aString[i]
            for x in range(len(aString)):#count the number of occurances for the same length
                if strLetter == aString[x]:
                    sameCnt += 1

            aString = aString.replace(strLetter, " ")#Replace all the matching letter

            myDict[strLetter] = sameCnt
    return aString, myDict

print(removePunctuation(strInfo))
        