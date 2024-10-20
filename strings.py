'''
string: collection of charecters
'''
sarname = " gopasina "
print(sarname.upper())    #GOPASINA
print(sarname.count("a"))   #2
print(len(sarname))   #10
print(sarname.strip())   #gopasina
name = "PRUDHVI"
print(name.lower())   #prudhvi
print(name.index("PRUDHVI"))    # 0 if the variable dosn't contains string throws error
print(name.find("PRUDHVI"))    #0 if the variable dosn't contains string returns -1

fullname = "Gopasina Prudhvi"
print(fullname.endswith("Prudhvi"))   #True
print(fullname.startswith("Prudhvi"))   #fasle
print(fullname.replace("Prudhvi","Prudhvi Raj"))   #Gopasina Prudhvi Raj
print(fullname.removeprefix("Gopasina"))   # Prudhvi
print(fullname.removesuffix("Prudhvi"))   #Gopasina 
print(fullname.split())   #['Gopasina', 'Prudhvi']
