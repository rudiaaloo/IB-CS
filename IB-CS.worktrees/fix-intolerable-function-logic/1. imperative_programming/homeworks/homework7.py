n = 1 
found = False
while not found:
    if (n**3 - 16) % 47 == 0: 
        found = True
        print(n) 
    else:
        n += 1

