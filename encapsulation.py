# '''
# Encapsulation: Weapping of a variables and methods in a single unit
#   ________________
#  /        |       \
# |variables|methods |
#  \________|_______/
 
# Encapsulation is possiable with access modifier 
# - Public
# - Private
# - Protected
# '''

class demo():
    def __init__(self,a,b):
        self.__value = a # private
        self._value1 = b #protected
class demo2(demo):
    def method(self):
        print(self._value1)
        print(self._value)
d = demo2(3,2)
d.method()
print(self._value1)

# output
'''
2
Traceback (most recent call last):
  File "c:\Users\pgopasina\TDW_KT_Python\TDW_KT_Python\encapsulation.py", line 23, in <module>
    d.method()
  File "c:\Users\pgopasina\TDW_KT_Python\TDW_KT_Python\encapsulation.py", line 21, in method
    print(self._value)
          ^^^^^^^^^^^
AttributeError: 'demo2' object has no attribute '_value'. Did you mean: '_value1'?
'''