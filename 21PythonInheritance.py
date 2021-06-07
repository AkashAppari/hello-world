#Python Inheritance

##Create a Parent Class
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        
    def printname(self):
        print(self.firstname,self.lastname)
x=Person("John","Doe")
x.printname()

##Create a Child Class
class Student(Person):
    pass
x=Student("Mike","Olsen")
x.printname()

###Single Inheritance
class Parent:
    def func1(self):
        print("This function is in parent class.")
class Child(Parent):
    def func2(self):
        print("This function is in child class.")

object= Child()
object.func1()
object.func2()

###Multiple Inheritance
class Mother:
    mothername=""
    def mother(self):
        print(self.mothername)
class Father:
    fathername=""
    def father(self):
        print(self.fathername)
class Son(Mother,Father):
    def parents(self):
        print("Father: ",self.fathername)
        print("Mother: ",self.mothername)
s1=Son()
s1.fathername="RAM"
s1.mothername="SITA"
s1.parents()

###Multilevel Inheritance
class Grandfather:
    grandfathername=""
    def grandfather(self):
        print(self.grandfathername)
class Father(Grandfather):
    fathername=""
    def father(self):
        print(self.fathername)
class Son(Father):
    def parent(self):
        print("GrandFather: ",self.grandfathername)
        print("Father: ",self.fathername)
s1=Son()
s1.grandfathername="Srinivas"
s1.fathername="Anksuh"
s1.parent()