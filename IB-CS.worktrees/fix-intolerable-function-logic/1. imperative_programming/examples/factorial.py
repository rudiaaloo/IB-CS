n = int(input("enter a positive integer:"))
if n > 0: 
    p = 1 #product 
    while n > 1: #no need for >= because n = 1 wont make change  
        p *= n #p = p*n 
        n -= 1 # same this as n = n - 1
    print(p) 
else:
    print("You did not enter a positive integer")
