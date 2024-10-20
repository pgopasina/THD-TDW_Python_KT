name ="prudhvi"
try:
    print(name)
except:
    print("error")
else:
    print("no error")
finally:
    print("always")

# we mention the type of error   
try:
    print(a+33)
except TypeError:
    print("this is a type error")
except ValueError:
    print("this is a type error")
    