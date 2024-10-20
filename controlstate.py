'''
decision making statements

if
else
elif
nested if
'''

age = 19

if age == 18:
    print( "you can vote")
    # if age > 18:
    #     print("you can vote")
else:
    print("you can not vote")
# -------------------------------------
if age == 18:
    print( "you can vote")
elif age > 18:
    print("you can vote")
else:
    print("you can not vote")
# ------------------------------------
if age == 18 or age >18:
    print( "you can vote")
else:
    print("you can not vote")