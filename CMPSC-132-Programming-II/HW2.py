# LAB2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement

import random
random.seed(2) 

class Course:

    def __init__(self, cid, cname, credits):
        self.cname = cname
        self.cid = cid
        self.credits = credits
        self.full = self.cid + "(" + str(self.credits) + "): " + self.cname #Creates formatted string
        

    def __str__(self):#Returns a formatted summary of the course as a string
        return self.full
        

    __repr__ = __str__

    def __eq__(self, other):
        if self is not None and other is not None: #Neither is None
            if self.full == other.full:
                return True
            else:
                return False
            
        elif self is None and other is None: #Both are None
            return True
        else: #Only 1 is None
            return False
        
class Catalog(Course):
    def __init__(self):
        self.courseOfferings = {}
        

    def addCourse(self, cid, cname, credits, capacity): #Creates a Course object with the parameters and stores it as a value in courseOfferings
        if cid not in self.courseOfferings:#Verifies if it exists
            crs = Course(cid, cname, credits)
            self.courseOfferings[cid] = (crs, capacity)
            return "Course added successfully"

        else:
            return "Course has already been added"

        

    def removeCourse(self, cid):
        if cid in self.courseOfferings:#verifies if course exists in dictionary
            self.courseOfferings.pop(cid, None)
            return "Course removed successfully"
        else:
            return "Course has already been removed or it isnt in the Catalog"
    
class Semester:
    

    def __init__(self, sem_num):
        self.smstrnm = sem_num
        self.courses = {}
        self.totalcred = 0
        


    def __str__(self):
        keys = ""
        if self.courses == {}:
            return "No courses"
        else:
            for x in self.courses:
                keys = keys + x + ", "  
            return keys[0:len(keys) - 2]

    __repr__ = __str__

    def addCourse(self, course):
        if course.cid not in self.courses:
            self.totalcred = self.totalcred + course.credits
            self.courses[course.cid] = course
            return "Course added successfully"

        else:
            return "Course already added"

    def dropCourse(self, course):
        if course.cid in self.courses:#verifies if course exists in dictionary
            self.totalcred = self.totalcred - course.credits
            self.courses.pop(course.cid, None)
            return "Course removed successfully"
        else:
            return "Course not found"

    @property
    def totalCredits(self):

        return self.totalcred

    @property
    def isFullTime(self):
        if self.totalcred == 12:
            return True
        else:
            return False

class Loan:

    def __init__(self, amount):
        self.amount = amount
        self.loan_id = self.__getloanID

    def __str__(self):
        return "Balance: $" + str(self.amount)

    __repr__ = __str__


    @property
    def __getloanID(self):
        return random.randrange(10000, 99999)

class Person:
    

    def __init__(self, name, ssn):
        self.nm = name
        self.socialsn = str(ssn)

    def __str__(self):
        return "Person('" + str(self.nm) + "', '***-**-" + self.socialsn[-4:] + "')"
        

    __repr__ = __str__

    def get_ssn(self):
        return self.socialsn

    def __eq__(self, other):
        if self is not None and other is not None: #Neither is None
            if self.socialsn == other.socialsn:
                return True
            else:
                return False
            
        elif self is None and other is None: #Both are None
            return True
        else: #Only 1 is None
            return False
        
class Staff(Person):

    def __init__(self, name, ssn, supervisor=None):
        self.staffsprvsr = supervisor
        super().__init__(name, ssn)

    def __str__(self):
        staffname = self.nm.split(" ")
        stafffrst = staffname[0][0]
        staffscnd = staffname[1][0]
        return "Staff('" + str(self.nm) + "', '" + "905" + stafffrst.lower() + staffscnd.lower() + self.socialsn[-4:] +"')"
        
    __repr__ = __str__


    @property
    def id(self):
        staffname = self.nm.split(" ")
        stafffrst = staffname[0][0]
        staffscnd = staffname[1][0]
        return "905" + stafffrst.lower() + staffscnd.lower() + self.socialsn[-4:]

    @property   
    def getSupervisor(self):
        return self.staffsprvsr

    def setSupervisor(self, new_supervisor):
        
        if new_supervisor != None:
            self.staffsprvsr = new_supervisor
            return "Completed!"
        else: 
            return None
        


    def applyHold(self, student):
        
        if student != None:
            student.hold = True
            return "Completed!"
        else: 
            return None
        

    def removeHold(self, student):
        if student != None:
            student.hold = False
            return "Completed!"
        else: 
            return None
        
    def unenrollStudent(self, student):
        if student != None:
            student.active = False
            return "Completed!"
        else: 
            return None

    def createStudent(self, person):
        return Student(person.nm, person.socialsn)

class Student(Person):

    def __init__(self, name, ssn, year = "Freshman"):
        random.seed(1)
        self.year = year
        self.semesters = {}
        self.hold = False
        self.active = True
        self.account = self.__createStudentAccount()
        super().__init__( name, ssn)

    def __str__(self):
        return "Student(" + self.nm + ", " + self.id + ", " + self.year + ")"

    __repr__ = __str__

    def __createStudentAccount(self):
        if self.active:
            self.account = StudentAccount(self)
            return self.account
        else:
            return None

    @property
    def id(self):
        dName = self.nm.split(" ")
        return (dName[0][0] + dName[1][0] + str(self.get_ssn()[-4:])).lower()

    def registerSemester(self):
        if not self.hold and self.active:
            currentSem = len(self.semesters) + 1
            self.semesters[currentSem] = Semester(currentSem)

            if currentSem <= 2:
                self.year = "Freshman"
            elif currentSem <= 4:
                self.year = "Sophomore"
            elif currentSem <= 6:
                self.year = "Junior"
            else:
                self.year = "Senior"

            return None
        else:
            return "Unsuccessful operation"

    def enrollCourse(self, cid, catalog, semester):
        if not self.hold and self.active:
            if cid in catalog.courseOfferings:
                if cid not in self.semesters[semester].courses:
                    crs = catalog.courseOfferings[cid][0]
                    self.semesters[semester].addCourse(crs)
                    self.account.chargeAccount(crs.credits * self.account.CREDIT_PRICE) #Charge the course amount
                    return "Course added successfully"
                else:
                    return "Course already enrolled"
            else:
                return "Course not found"  
        else:
            return "Unsuccessful operation" 


    def dropCourse(self, cid):
        if not self.hold and self.active:
            currentSem = len(self.semesters)
            if cid in self.semesters[currentSem].courses:
                crs = self.semesters[currentSem].courses[cid]
                self.semesters[currentSem].dropCourse(crs)
                self.account.makePayment(crs.credits * self.account.CREDIT_PRICE / 2) #Return only half of the course cost
                return "Course dropped successfully"
            else:
                return "Course not found"
        else:
            return "Unsuccessful operation" 

    def getLoan(self, amount):
        if self.active:
            currentSem = len(self.semesters)
            if self.semesters[currentSem].isFullTime:
                l = Loan(amount)
                self.account.loans[l.loan_id] = l
                self.account.makePayment(amount)
            else:
                return "Not full-time”"
        else:
            return "Unsuccessful operation"      
    
    def getName(self):
        return self.nm
        
class StudentAccount:

    CREDIT_PRICE = 1000
    
    def __init__(self, student):
        self.stdnt = student
        self.balance = 0
        self.loans = {}        


    def __str__(self):
        strReturn = "Name: " + self.stdnt.getName()
        strReturn = strReturn + "\nID: " + self.stdnt.id
        strReturn = strReturn + "\nBalance: $" +str(self.balance)

        return strReturn

    __repr__ = __str__


    def makePayment(self, amount):
        self.balance = self.balance - amount
        return self.balance

    def chargeAccount(self, amount):
        self.balance = self.balance + amount
        return self.balance



if __name__=='__main__':
    import doctest
    doctest.testmod()  # OR
    #doctest.run_docstring_examples(Course, globals(), name='HW22',verbose=True) 
    # replace Course for the class name you want to test