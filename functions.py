def func(a,b,c):
    print("this is function", a,b,c)
func(3,1,2) 

# orbitary arguments
# if we send multipale arguments for single parameter
# we have use * before the parameter
# arguments are stored in tuple
def func1(*a):
    print("this is function",a)
func1(1,2,3) 

# keyword arguments
# if we send multipale key:value pair of arguments for single parameter
# we have use ** before the parameter
# arguments are stored in dictionary
def func2(**a):
    print("this is function",a)
func2(a=1,b=2) 

# nested function
def outer():
    print("this is outer function")
    def inner():
        print("this is inner function")
    inner()
outer() 

def add(a,b):
    print(a+b)
    
def sub(a,b):
    print(a-b)