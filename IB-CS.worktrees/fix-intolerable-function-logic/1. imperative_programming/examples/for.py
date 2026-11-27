k = 1 
for y in range(1, 41): 
    m = y 
    if y % 4 == 0:
        m = -1 
    print(m, end=' ')
print() ##why do we need this print statement?