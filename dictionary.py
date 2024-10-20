D = {}
print(type(D))

d = {1:"abc", 21:777,"name":"prudhvi"}
print(d.get(1))
print(d.keys())
print(d.values())
print(d.items())
d.update({"roll":"dev"})
print(d)

for i,j in d.items():
    print(i,j)