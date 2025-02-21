#  Problem 1: Define a python class person with instance object variables name and age. Set instance object variable in
#   __init__() method. Also define show() method to display name and age of a person  '''

class person:
    def __init__(self, name = None , age = None):
        self.name = name
        self.age = age

    def setName(self,name):
        self.name = name

    def setAge(self,age):
        self.age = age

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

p1 = person()    
p2 = person()

p1.setName("vaishnavi")
p1.setAge(21)

print("name is : ",p1.getName())
print("age is : ",p1.getAge())

# ===========================================================================================

# Problem 2 : DEfine a class circle with instacne object variable radius. Provide setter and getter for radius.
# Also define getArea() and getCircumference() methods.

import math

class circle:
    def __init__(self, radius = None, area = None, circumference = None ):
        self.radius = radius
        self.area = area
        self.circumference = circumference

    def setRadius(self, radius):
        self.radius =  radius

    # def setArea(self, area):
    #     self.area = area
    
    # def setCircumference(self, circumference):
    #     self.circumference = circumference

    def getRadius(self):
        return self.radius 

    def getArea(self):
        return math.pi * self.radius ** 2           #pi*r**2 : r**2 = square of r

    def getCircumference(self):
        return 2 * math.pi * self.radius


c1 = circle()

c1.setRadius(5)
print("radius of c1 is: ", c1.getRadius())
print("area of c1 is: ", c1.getArea())
print("Circumference of c1 is : ",c1.getCircumference())

c2 = circle()

c2.setRadius(15)
print("radius of c2 is: ", c2.getRadius())
print("area of c2 is: ", c2.getArea())
print("Circumference of c2 is : ",c2.getCircumference())


# =======================================================================================================================================

# Problm 3 : Define a class rectangle with length and breadth as instance object variable. Provide setDimensions(), showDimensions  
# and getArea() method in it.

import math 

class rectangle:
    def __init__(self, length = None, breadth = None):
        self.length = length
        self.breadth = breadth

    def setLength(self, length):
        self.length = length

    def setBreadth(self, breadth):
        self.breadth = breadth

    # def getLength(se

    def setDimensions(self, length, breadth):
        if length > 0 and breadth > 0:
            self.length = length
            self.breadth = breadth
    
    def setArea(self, area):
        self.area = area

    def showDimensions(self):
        print(f"length of reactangle {self.length} and breadth is {self.breadth}")

    def getArea(self):
        return self.length * self.breadth


r1 = rectangle(10, 20)
# print(r1.setLength(10))
# print(r1.setBreadth(20))
r1.showDimensions()
print(r1.getArea())

r2 = rectangle(15, 15)
print("updated dimensions are : ")
r2.showDimensions()
print(r2.getArea())



# ==============================================================================================================================================================

# Problem 4 : Define a class book with instance object variable bookid, title and price , Initialise them via __init__() method. 
# Also define method to show book variables

class book:
    def __init__(self, bookid = None, title = None, price = None):
        self.bookid = bookid
        self.title = title
        self.price = price

    # def setBookid(self, bookid):
    #     self.bookid = bookid

    # def setTitle(self, title):
    #     self.tite = title

    # def setPrice(self, price):
    #     self.price = price

    # def showBookid(self, bookid):
    #     return bookid

    # def showTitle(self, title):
    #     self.title = title

    # def showPrice(self, price):
    #     self.price = price

    def showBookDEtails(self):
        print(f"book id is : {self.bookid}")
        print(f"Title of the book is : {self.title}")
        print(f"and the price of the book is : {self.price}")


b1 = book(1, "fairy tails", 250)
print(b1.showBookDEtails())

b2 = book(2, "our intertwine fates", 600)
print("another book details are: ")
b2.showBookDEtails()



# Problem 5 : Define class team with instance object variable a list of team member names. provide methods to input member names nd display member name

class team:
    def __init__(self):
        self.members = []

    def addMembers(self):
        # self.name = name
        num = int((input("enter the number of the team members : ")))
        for _ in range (num):   
            name = (input("the name of the team members : "))
            self.members.append(name)

    def showMembers(self):
        if self.members:
            print("team members : ")
            for idx , members in enumerate(self.members , start = 1):
                print(f"{idx} : {members}")
        
        else :
            print("No mmber found!!..")

t1 = team()
t1.addMembers()

t1.showMembers()