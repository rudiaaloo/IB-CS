#iterables
if n > 0: 
    p = 1 #product 
    for k in range(2, n + 1): #upperbound = n +1 
        p *= k #p = p*n 
    print(f'{n}! = {p}')
else: 
    print("given integer  is ")