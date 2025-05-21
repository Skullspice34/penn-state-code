# LAB 5
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement


from turtle import right


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:

    def __init__(self):
        self.root = None


    def insert(self, value):
        if self.root is None:
            self.root= Node(value)
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
        if(value < node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:   
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    
    @property
    def printInorder(self):
        if self.isEmpty(): 
            return None
        else:
            self._inorderHelper(self.root)
        
    def _inorderHelper(self, node):
        if node is not None:
            self._inorderHelper(node.left) 
            print(node.value, end=' : ') 
            self._inorderHelper(node.right)         


    def mirror(self):
        # Creates a new BST that is a mirror of self: 
        #    Elements greater than the root are on the left side, and smaller values on the right side
        # Do NOT modify any given code
        if self.root is None:
            return None
        else:
            newTree = BinarySearchTree()
            newTree.root = self._mirrorHelper(self.root)
            newTree.printInorder
            return newTree
        




    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False



    def _mirrorHelper(self, node):
        nn = Node(node.value)

        if node.right != None:
            nn.left = self._mirrorHelper(node.right)
            
        
        if node.left != None:
            nn.right = self._mirrorHelper(node.left)

        return nn



        


    @property
    def getMin(self): 
        if self.root.value != None:
            return self.getMinMaxHelper(self.root)[0]
        
        else:
            return None

    @property
    def getMax(self): 
        if self.root.value != None:
            return self.getMinMaxHelper(self.root)[1]
        
        else:
            return None

        
    def getMinMaxHelper(self, node):
        #Created a minmax function since both functions are similar
        minMax = [node.value, node.value]
        #minMax[0] is minimum value, minMax[1] is maximum value

        #Check left Node
        if node.left != None:
            newMinMax = self.getMinMaxHelper(node.left)
            minMax = self.compareMinMax(minMax, newMinMax)
        
        #Check right Node
        if node.right != None:
            newMinMax = self.getMinMaxHelper(node.right)
            minMax = self.compareMinMax(minMax, newMinMax)
            
        return minMax

    def compareMinMax(self, minMax, newMinMax):
        #Compare and return the min max
        if minMax[0] > newMinMax[0]:
            minMax[0] = newMinMax[0]

        if minMax[1] < newMinMax[1]:
            minMax[1] = newMinMax[1]
            
        return minMax

    def __contains__(self, value):#Checks if a value is present in the tree by overloading the in operator.
        return self.containsHelper(self.root, value)

    def containsHelper(self, node, value):

        if node.value == value:
            return True

        else:
            #Check left Node
            if node.left != None:
                if self.containsHelper(node.left, value):
                    return True
            
            #Check right Node
            if node.right != None:                
                if self.containsHelper(node.right, value):
                    return True                
            
            return False


    


    def getHeight(self, node):#Gets the height of a node in the tree.
        heightL = -1
        heightR = -1

        #Check left Node
        if node.left != None:
            heightL = self.getHeight(node.left)
                    
        #Check right Node
        if node.right != None:
            heightR = self.getHeight(node.right)     
        
        if heightL > heightR:
            return heightL + 1

        else:
            return heightR + 1
            



