neg = []
pos = []

while (int := (int(input("enter an integer")))) != 0: #think about it as, its gonna keep running while xyz is not 0
    if int < 0:
        neg.append(int)
    elif int == 0:
        print(neg, pos)
    else:
        pos.append(int)
        