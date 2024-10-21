'''
Inheritance: Accessing parent class propertices into child classes
Type of Inheritance
-Single inheritance
-multilevel inheritance
-multiple inheritance
-hierachical inheritance
'''
# Single inheritance
print('Single inheritance-------')
class Parent():
    def methodparent(self):
        print("I'm the parent")
class Child(Parent):
    def methodchild(self):
        print("I'm the child")

classchild = Child()
classchild.methodparent()
classchild.methodchild()

# multilevel inheritance
print('multilevel inheritance-------')
class Grandfather():
    def methodgf(self):
        print("I'm the grandfather")
class Parent1(Grandfather):
    def methodparent1(self):
        print("I'm the parent1")
class Child1(Parent1):
    def methodchild1(self):
        print("I'm the child1")
classchild1 = Child1()
classchild1.methodchild1()
classchild1.methodparent1()
classchild1.methodgf()

# multiple inheritance
print('multiple inheritance-------')
class Father():
    def methodfather(self):
        print("I'm the father")
class Mother():
    def methodmother(self):
        print("I'm the mother")
class Child2(Father, Mother):
    def methodchild2(self):
        print("I'm the child2")
classchild2 = Child2()
classchild2.methodchild2()
classchild2.methodfather()
classchild2.methodmother()

# hierachical inheritance
print('hierachical inheritance-------')
class Father1():
    def methodfather1(self):
        print("I'm the father1")
class Child3(Father1):
    def methodchild3(self):
        print("I'm the child3")
class Child4(Father1):
    def methodchild4(self):
        print("I'm the child4")
classchild3 = Child3()
classchild3.methodchild3()
classchild3.methodfather1()

classchild4 = Child4()
classchild4.methodchild4()
classchild4.methodfather1()

# Output
'''
Single inheritance-------
I'm the parent
I'm the child
multilevel inheritance-------
I'm the child1
I'm the parent1
I'm the grandfather
multiple inheritance-------
I'm the child2
I'm the father
I'm the mother
hierachical inheritance-------
I'm the child3
I'm the father1
I'm the child4
I'm the father1
'''