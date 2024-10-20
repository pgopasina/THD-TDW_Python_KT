s = {1,22,'prudhvi'}
print(type(s))
s.add(1212)
print(s)
s.update({1,2,4,5,6})
print(s)
s.pop()
print(s)
s.remove(22)
print(s)

# <class 'set'>
# {1, 1212, 22, 'prudhvi'}
# {1, 2, 4, 5, 6, 'prudhvi', 22, 1212}
# {2, 4, 5, 6, 'prudhvi', 22, 1212}
# {2, 4, 5, 6, 'prudhvi', 1212}

set1 = {1,2,3,4}
set2 = {1,2,3,4,5,6,7,8}
print(set1.union(set2))
print(set1.difference(set2))
print(set1.intersection(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))

for i in set1:
    print(i)