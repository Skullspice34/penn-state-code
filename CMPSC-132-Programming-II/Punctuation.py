strInfo = "Dots..........Comas,,,,,,,,Questions?????#%"

myDict = {}

for i in range(len(strInfo)):
    
    if not strInfo[i].isalpha() and strInfo[i] != " ":
        if strInfo[i] not in myDict:#check if the value isn't already added to the dictionary
            sameCnt = 0
            strLetter = strInfo[i]
            for x in range(len(strInfo)):#count the number of occurances for the same length
                if strLetter == strInfo[x]:
                    sameCnt += 1

            strInfo = strInfo.replace(strLetter, " ")#Replace all the matching letter

            myDict[strLetter] = sameCnt

strReturn = [strInfo, myDict]
print(strReturn)