# LAB4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class SortedLinkedList:

    def __init__(self):   # You are not allowed to modify the constructor
        self.head=None
        self.tail=None

    def __str__(self):   # You are not allowed to modify this method
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out) 
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__


    def isEmpty(self):
        return self.head == None

    def __len__(self):
        count=0
        current=self.head
        while current:
            current=current.next
            count+=1
        return count

                
    def add(self, value):
        if self.head == None:
            self.head = Node(value)
        
        elif self.tail == None:
            
            if value < self.head.value:
                self.tail = self.head
                self.head = Node(value)
            
            else:
                self.tail = Node(value)
            
            self.head.next = self.tail
            
        else:
            current=self.head
            prvs = None
            if value >= self.tail.value:#If it is the last node
                tl = self.tail
                self.tail = Node(value)
                tl.next = self.tail
                return
            
            while current:
                if value < current.value:
                    if prvs == None:#If it's the first node
                        self.head = Node(value)
                        self.head.next = current
                    else:
                        prvs.next = Node(value)
                        prvs.next.next = current
                    current = None
                        
                else:
                    prvs = current
                    current = current.next

    def replicate(self):

        NewLst = SortedLinkedList()
        current=self.head
        while current:
            t = current.value
            if t < 0 or t % 1 != 0:
                t = 2
            elif t < 2:
                t = 1

            for i in range(0,t):
                NewLst.add(current.value)

            current=current.next
            
        return NewLst

        
    def removeDuplicates(self):
        current = self.head.next
        prvs = self.head
        
        while current:
            if prvs.value == current.value: 
                current = prvs.next
                prvs.next = current.next
            else:
                prvs = current
                current = current.next



