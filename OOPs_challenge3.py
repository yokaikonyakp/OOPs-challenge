# Challenge 3: Implement the Complete Student Class

# 🔴In this challenge, implement a student class
# Problem statement

# Implement the complete Student class by completing the tasks below

# Task

# 👉 Implement the following properties as private:

# • name
# • rollNumber
# 👉 Include the following methods to get and set the private properties above:

# • getName()
# • setName()
# • getRollNumber()
# • setRollNumber()
# 👉 Implement this class according to the rules of encapsulation.

# Input - Checking all the properties and methods

# Output - Expecting perfectly defined fields and getter/setters

# Note: Do not use initializers to initialize the properties. Use the set methods to do so.

# If the setter is not defined properly, the corresponding getter will also generate an error even if the getter is defined properly.


class Student:
    def __init__(self):

        #The properties "name" and "rollNumber" are defined as private by prefixing them with single underscore.
        #initial values of these properties are set to "None"
        self._name = None
        self._rollNumber = None

#using getter method to retrive the values of private properties
#and setter methods to set the values of private properties
    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getRollNumber(self):
        return self._rollNumber

    def setRollNumber(self, rollNumber):
        self._rollNumber = rollNumber



student = Student()
student.setName("Yokai Konyak P")
student.setRollNumber(140223)

name = student.getName()
rollNumber = student.getRollNumber()

print(name)       
print(rollNumber)  
