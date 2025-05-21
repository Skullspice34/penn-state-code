# LAB2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement

import random
from tabnanny import check
from tkinter import Y

class Fibonacci:


    def __init__(self, start = 0, nextnum = 1):
        self.start = start
        self.nextnum = nextnum


    def next(self):#goes to the next Fibonacci
        return Fibonacci(self.nextnum, self.nextnum + self.start) 


    def __repr__(self):
        return f"<Fibonacci object>, value = {self.start}"





class Vendor:

    def __init__(self, name):

        self.name = name
        self.vendor_id = random.randint(999, 999999)
    
    def install(self):
        return VendingMachine()
    
    def restock(self, machine, item, amount):
        return machine._restock(item, amount)
        


class VendingMachine:

    def __init__(self):
        self.stock = {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]} 
        self.balance = 0



    def purchase(self, item, qty=1):
        if self.isStocked():#checks if machine is stocked
            if item in self.stock:#cheques if item exists
                if qty != None and self.balance >= self.stock[item][0]:#checks if enough money in balance to buy the item
                    if self.balance - self.stock[item][0] * qty < 0:# checks if balance less than the amount needed
                        return "Not enought money to buy" + str(qty) + str(item)
                    elif self.stock[item][1] == 0:  #Checks if item available                      
                        return "Item out of stock"
                    elif qty > self.stock[item][1] and self.stock[item][1] != 0: #Checks if there are enough items in machine to give to the customer
                        return "Current " + str(item) + " stock: " + str(self.stock[item][1]) + ", try again"  
                    else:#succsesful transaction
                        self.stock[item][1] = self.stock[item][1] - qty
                        return "Item dispensed, take your $" + str(self.balance - (self.stock[item][0] * qty)) + " back"
                elif self.balance == 0:#checks if money = 0
                    return "Not enough money, please deposit $" + str(self.stock[item][0])
                elif self.balance < self.stock[item][0]:# checks if balance less than the amount needed
                    return "Not enough money, please deposit " + str(self.balance - self.stock[item][0])

                return "Please depoit $" + str(self.stock[item][0])
                
            else:
                return "Invalid item"
        else:
            return "Machine out of stock"
   


    def deposit(self, amount):#saves amount entered
        self.balance = amount
        return "Balance: $" + str(self.balance)
        


    def _restock(self, item, stock):#adds an item of you choise a "stock" amount of times
        self.stock[item][1] = self.stock[item][1] + stock
        return "Current " + str(item) + " stock: " + str(self.stock[item][1])


    
    def isStocked(self):
        for i in self.stock:#checks if all items are out of stoked
            if self.stock[i][1] != 0:#returns true if at least 1 item is available
                return True 
        return False

    
    def getStock(self):#returns what the machine has of every item
        return (self.stock)


    def cancelTransaction(self):
        if self.balance != 0: #if balance isnt 0 then return all the money
            oldBalance = self.balance
            self.balance = 0
            return "Take your $" + str(oldBalance) + " back"
        

   
       



class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line: 
    
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2
                

    def _str_(self):#returns the equuation of a line
        b = round((self.p1.y - self.getSlope()*self.p1.x), 3)
        if self.getSlope() == 0:#checks if slope = 0
            return "Undefined"

        elif b == 0:#checks if b = 0
            return "y = " + str(self.getSlope())
        
        elif b < 0:#checks if b less than 0
            return "y = " + str(self.getSlope()) + "x - " +  str(-1*b)
        return "y = " + str(self.getSlope()) + "x + " + str(b)



    def __repr__(self) -> str: #returns the equuation of a line
        b = round((self.p1.y - self.getSlope()*self.p1.x), 3)
        if self.getSlope() == 0:#checks if slope = 0
            return "Undefined"

        elif b == 0:#checks if b = 0
            return "y = " + str(self.getSlope())
        
        elif b < 0:#checks if b less than 0
            return "y = " + str(self.getSlope()) + "x - " +  str(-1*b)
        return "y = " + str(self.getSlope()) + "x + " + str(b)
        


    def getDistance(self):#returns the distance calculaton
        return round(( ( ( (self.p2.x - self.p1.x )**2) + ( (self.p2.y - self.p1.y)**2) )**0.5), 3)
       
    

    def getSlope(self):#returns the slope calculaton
        return round((self.p2.y - self.p1.y) / (self.p2.x - self.p1.x), 3)
    






if __name__=='__main__':
    import doctest
    doctest.testmod()  # OR
    #doctest.run_docstring_examples(Fibonacci, globals(), name='LAB2',verbose=True)
# replace Fibonacci for the class name you want to test
 