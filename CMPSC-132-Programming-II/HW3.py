# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement


from pickle import TRUE
from runpy import _TempModule
from xml.dom.minidom import Element


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:

    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):#Tests to see whether this stack is empty or not.
        if self.top != None:
            return False

        else:
            return True


    def __len__(self): #Returns the number of elements in this stack.
        num = 0
        crrnt = self.top
        while crrnt:
            crrnt = crrnt.next
            num+=1
        return num

    def push(self,value): #Adds a new node with value=item to the top of the stack. Nothing is returned by this method.
        nwn = Node(value)
        nwn.next = self.top
        self.top = nwn

     
    def pop(self): #Removes the top node from the stack and returns that node’s value (not the Node object).
        x = self.top
        if self.top == None:
           return
        else:
            self.top = self.top.next
            return x.value

    def peek(self):
        if self.top == None:
            return
        else:
            return self.top.value


#=============================================== Part II ==============================================


class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        n = txt.strip(" ")
        try:
            float(n)
            return True
        except:
            return False

    def _getPostfix(self, txt):
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        blRun = True
        postfix = ""
        opSeq = {"(" : 0, "+" : 1, "-": 1, "*" : 2, "/" : 2, "^" : 3}
        lastnum = ""

        for num in txt.split(" "):
            if num != "":# Check if not empty
                if self._isNumber(num):
                    if self._isNumber(lastnum):
                        return #"Error: There are 2 consecutive numbers without an operator"
                    else:
                        postfix = postfix + str(float(num)) + " "
                
                elif num != ")":

                    if not self._isNumber(lastnum) and num != "(" and lastnum != "(" and num != ")" and lastnum != ")" and lastnum != "":
                        return #"Error: There are 2 consecutive operators without a number"

                    if num == "(" and lastnum == ")" or num == "(" and self._isNumber(lastnum):
                        return None #No operators btween ()

                    blRun = TRUE

                    while (blRun):
                        
                        if postfixStack.isEmpty() or (num == "^" and postfixStack.peek() == "^"): #If empty push operator
                            postfixStack.push(num)
                            blRun = False

                        elif opSeq.get(num) == None: #Operator not allowed
                            return #"Invalid character detected"
                        
                        elif opSeq.get(postfixStack.peek()) < opSeq.get(num) or num == "(":#The operator is less
                            postfixStack.push(num)
                            blRun = False

                        elif opSeq.get(num) == opSeq.get(postfixStack.peek()) and num != postfixStack.peek():#The operator is equal
                            postfix = postfix + postfixStack.pop() + " "                
                            postfixStack.push(num)
                            blRun = False

                        else:
                            if postfixStack.peek() != "(":
                                postfix = postfix + postfixStack.pop() + " "

                            else:
                                postfixStack.pop()

                else: #It's a ")" so look for the starting "("
                    blRun = TRUE
                    while (blRun):
                        
                        if postfixStack.isEmpty():
                            return None #No startig '('

                        elif postfixStack.peek() == "(":  #Found the starting "("
                            postfixStack.pop()
                            blRun = False

                        else:
                            postfix = postfix + postfixStack.pop() + " "
                
                #Store the last num to check if there are 2 numbers without operator
                lastnum = num

        if not self._isNumber(num) and num != ")":
            return #"Error: It cannot end with an operator."

        else:
            #Empty Stack
            blRun = TRUE
            while (blRun):
                if postfixStack.isEmpty():
                        blRun = False

                elif postfixStack.peek() == "(":
                    return #"Error. There is a '(' without a matching ')'"

                else:
                    postfix = postfix + postfixStack.pop() + " "
                

            return postfix.strip(" ")     
            

    @property
    def calculate(self):


        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression
        postFix = self._getPostfix(self.__expr)
        expCnt = 0

        if postFix != None:
            for num in postFix.split(" "):
                if self._isNumber(num):
                    calcStack.push(num)

                else:
                    x = float(calcStack.pop())

                    if num == "+":                    
                        x = float(calcStack.pop()) + x 
                    elif num == "-":                    
                        x = float(calcStack.pop()) - x 
                    elif num == "*":                    
                        x = float(calcStack.pop()) * x 
                    elif num == "/":                    
                        x = float(calcStack.pop()) / x 
                    elif num == "^":                    
                        x = float(calcStack.pop()) ** x

                    calcStack.push(x)

            return float(calcStack.pop())
        
        else:
            return None #No expresion was saved





#=============================================== Part III ==============================================

class AdvancedCalculator:
    
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        
        if not str.isnumeric(word[0]) and str.isalpha(word[0]) and str.isalnum(word):
            return True
        else:
            return False

    def _replaceVariables(self, expr):
        
        # YOUR CODE STARTS HERE

        x = Calculator()

        for l in expr.split(" "):

            if not x._isNumber(l) and l != " " and l != "+" and l != "-" and l != "*" and l != "/" and l != "^" and l != ")" and l != "(": 
                if l in self.states:
                    expr = expr.replace(l, str(self.states[l]))
                else:
                    return None

        return expr
    
    def calculateExpressions(self):
        self.states = {} 
        calcObj = Calculator()     # method must use calcObj to compute each expression
        outDict = {}
        for exp in self.expressions.split(";"):

            if "return" in exp:# found the return
                newExpr = self._replaceVariables(exp.replace("return ", ""))
                if newExpr == None:
                    return None #The variable has not been declared
                else:
                    calcObj.setExpr(newExpr)
                    outDict['_return_'] = calcObj.calculate

            else:#split and calculate 
                sExp = exp.split("=")
                sExp[0] = sExp[0].strip(" ")

                #Use the replace function before sending to Calculate
                newExpr = self._replaceVariables(sExp[1].strip(" "))
                if newExpr == None:
                    self.states = {}
                    return None #The variable has not been declared
                else:
                    calcObj.setExpr(newExpr)
                self.states[sExp[0]] = calcObj.calculate

                outDict[exp] = self.states.copy()

        return outDict
                

            

