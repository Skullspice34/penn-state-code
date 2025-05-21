## Lab 0

def sumSquares(numList):
    Add = 0
    for num in numList:
        if (num > 5 and num < 500) or (num % 4 == 0):
            Add += num * num
    return Add
