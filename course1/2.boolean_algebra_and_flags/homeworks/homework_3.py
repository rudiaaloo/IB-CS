found = False 
n = 1

while not (0 < (s := int(input('Enter a positive integer: ')))):
    pass

while not found:
    calc = (n**3 - 10*n**2) 
    if (calc > s): 
        found = True 
    else:
        n += 1 

print(n, calc) 