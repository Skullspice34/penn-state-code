# LAB3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement
# All functions should NOT contain any for/while loops or global variables. Use recursion, otherwise no credit will be given

from ast import Return
from itertools import count
from re import M
from ssl import ALERT_DESCRIPTION_ACCESS_DENIED


def get_count(aList, item):


    if aList == None and item == None:
        return "Please write a list and an item"
    elif aList == None or aList == []:
        return "There is nothing in the list."
    else:
        tm = item
        mbtm = aList[0] 

        if mbtm == item:
            rst = 1
        else:
            rst = 0

        if len(aList) > 1:
            rst += get_count(aList[1:], tm) 
            return rst
        else:#returns the count 
            return rst


            


        

    
    
def replace(numList, old, new):
 
    numcopy = numList[:]
    if old not in numcopy:# if the number dosent exist in the list
        return numcopy
    else:
        numcopy[numcopy.index(old)] = new #replaces old with new
        return replace(numcopy, old, new)


def cut(aList):

    num = aList[0]
    if num < 0: #If there is a negative number
        num = num * -1
        if num - 1 >= len(aList): 
            return []
        else:
            return cut(aList[num:])
    else: #There are no negative numbers
        if len(aList) > 1:
            res = cut(aList[1:])
            res.insert(0, num) 
            return res
        else:
            return aList[:]


def neighbor(n):

    nmbr = n % 10
    othernmbr = (n // 10) % 10
    if n < 10:
        return n
    elif othernmbr == nmbr: #check if last number equal to the second to last one and eliminates it 
        return neighbor(n // 10)
    elif othernmbr != nmbr:#
        return neighbor(n // 10) * 10 + nmbr
        
        
        




        
        