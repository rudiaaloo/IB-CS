lst = list(range(10))
print(10 in lst) 

lst = [10 - abs(x-3) for x in range(10)]
print(lst) 
val = 8 #this would give us how many times 8 is in the list, which is 1 time
print(lst.count(val)) 
print(lst.index(val)) #this would give us the index of the first occurrence of 8 in the list, which is 7
