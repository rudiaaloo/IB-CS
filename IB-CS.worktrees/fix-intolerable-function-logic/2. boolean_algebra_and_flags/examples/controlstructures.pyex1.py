A = int(input("please give a value A:" ))
B= int(input("please give a value B:" ))
C= int(input("please give a value C:" ))
D= int(input("please give a value D:" ))

AB = A + B 
AC = A - C
BC = B - C

if AB * BC > 0:
    RESULT = B 
elif AB* AC < 0:
    RESULT = A
else:
    RESULT = C
print("The result is:", RESULT)