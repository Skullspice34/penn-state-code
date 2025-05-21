# HW1


##RECTANGLE FUNCTION

p = 14
a = 10

def rectangle(perimeter,area):
    if perimeter < area or perimeter > area: # makes sure its not a square
        if perimeter == 0 or area == 0: #verifies if either the perimeter or the area is 0
            return "False"
        else:
            add = perimeter // 2 #divides the perimeter by 2
            frstnum = 1
            for frstnum in range(1, add): #checks every posible sum
                scndnum = add - frstnum 
                if frstnum * scndnum == area and frstnum > scndnum: #checks if both numbers multiplied are equal to the area, and prints out frstnum if its the bigger number
                    return frstnum
                elif frstnum * scndnum == area and frstnum < scndnum:#checks if both numbers multiplied are equal to the area, and prints out scndnum if its the bigger number
                    return scndnum
            
    
    else:# if anything else is writen, prints false
        return "False" 


##INVERT FUNCTION

OrgnlDic = {'123-456-78':'Sara', '987-12-585':'Alex', '258715':'sara', '00000':'Alex'}

def invert(d):
    InvrtdDic = {}
    dplctKey = []
    for i in d:
        if not d[i] in InvrtdDic and d[i] not in dplctKey: #inverts the value with the index
            InvrtdDic[d[i]] = i
        else: #cheques if the index already exists and eliminates both copies
            dplctKey.append(d[i])
            InvrtdDic.pop(d[i], None)
    return InvrtdDic


##SUCCESSORS FUNCTION

def successors(filename):
    
    with open(filename) as f: 
        contents = f.read()
        y = contents.replace("\n", " ")#elemiates enters
        x = y.replace(".", " . ")#makes spaces before and after punctuation
        w = x.replace(",", " , ")
        q = w.replace("!", " ! ")
        e = q.replace("?", " ? ")
        t = e.replace(":", " : ")
        r = e.replace(";", " ; ")#^^^^^^^^^^^^^^^^^^
        words = r.split(' ') #everithing is divided by spaces
        strPred = '.'

        newDict = {}

        for x in words:
            if x != "":#filters out multiple spaces
                if strPred in newDict:#verifies if x exists in dictionary
                    if not x in newDict[strPred]:#verifies if the value already exist
                        newDict[strPred].append(x)
                else:#add x to dictionary
                    newDict[strPred] = [x]
                strPred = x

    return newDict




##GET POSITION FUNCTION

dgt =  3
nmbr = 1549

def getPosition(num, digit):
    for pos in range(1, num):    
        a = num % 10 #saves the rightmost digit
        if a == digit: #cheques if a is equal to digut
            return pos
        else:
            num = num // 10 #eliminates the rightmost digit
            pos = pos + 1 #caunts the position

    return "False"


##HAILSTONE FUNCTION
    
hail = 1000

def hailstone(num):
    hlstn = [num]
    for x in range(num + 10):
        if num % 2 == 0: # if number even divide by 2
            num = num // 2
            hlstn.append(num)
        elif num == 1: #when num = 1 stop the loop
            return hlstn
        else: # if number odd multiply by 3 then add 1
            num = 3 * num + 1
            hlstn.append(num)


##LARGE FACTOR FUNCTION

anum = 1

def largeFactor(num):
    div = 1
    large = 1
    for div in range(1, num): # divides by every number
        if num % div == 0: #cheques if number equals 0
            large = div
    return large


