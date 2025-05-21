# HW4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement
# You might add additional methods to encapsulate and simplify the operations, but they must be
# thoroughly documented


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


    # Modify the insert and _insert methods to allow the operations given in the PDF
    # Document all the modifications done
    def insert(self, value):
        if self.root is None:
            srtd = sorted(value)
            strng = ""
            self.root = Node({strng.join(srtd):[value]})
        else:
            self._insert(self.root, value)



    def _insert(self, node, value):
        #Adds a space to be able to compare words that are shorter or longer than each other.
        sValue = "".join(sorted(value)) + " "
        strKey = list(node.value.keys())[0] + " "

        if sValue == strKey:
            #Check if exists already
            if value not in node.value[strKey.strip()]:
               node.value[strKey.strip()].append(value)
            
        else:
            iV = 0
            blStp = False

            #Compare each letter value
            while (sValue[iV] == strKey[iV] and not blStp):
                iV += 1

                #If length exceded then stop.
                if iV < len(sValue) - 2 or iV < len(strKey) - 2: 
                    blStp = True
            
            if ord(sValue[iV]) < ord(strKey[iV]):
                #If it does not exist the add it
                if(node.left == None):
                    node.left = Node({sValue.strip():[value]})

                else:
                    self._insert(node.left, value)
            else:   
                if(node.right == None):
                    node.right = Node({sValue.strip():[value]})
                
                else:
                    self._insert(node.right, value)


    def isEmpty(self):
        return self.root == None

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



class Anagrams:

    
    def __init__(self, word_size):
        self.wrdsz = word_size
        self._bst = BinarySearchTree()




    def create(self, file_name):
        with open (file_name) as f:
            contents = f.read().split()
        for i in contents:
            if len(i) <= self.wrdsz:
                self._bst.insert(i)
            


    def getAnagrams(self, word):
        if self._bst.root is None:
            return "'No match'"
        else:
            r = self.getAnagramhelper(self._bst.root, word)

            if r == None:
                return "'No match'"

            else: 
                return r

            


    def getAnagramhelper(self, nd, word):
        #Adds a space to be able to compare words that are shorter or longer than each other.
        AwrdValue = "".join(sorted(word)) + " "
        AwrdstrKey = list(nd.value.keys())[0] + " " 


        if AwrdValue == AwrdstrKey:
            #Check if exists already
            return nd.value[AwrdstrKey.strip()]

        else:
            Ai = 0
            AblStp = False

            #Compare each letter value
            while (AwrdValue[Ai] == AwrdstrKey[Ai] and not AblStp):
                Ai += 1

                #If length exceded then stop.
                if Ai < len(AwrdValue) - 2 or Ai < len(AwrdstrKey) - 2: 
                    AblStp = True
            
            if ord(AwrdValue[Ai]) < ord(AwrdstrKey[Ai]):
                #If it does not exist return No match
                if(nd.left == None):
                    return "'No match'"

                else:
                    return self.getAnagramhelper(nd.left, word)
            else:   
                if(nd.right == None):
                    return "'No match'"
                
                else:
                    return self.getAnagramhelper(nd.right, word)

