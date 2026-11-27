lst = [x % 3 for x in range(10)]
#list is iterable in itself 
for x in lst:
    print(x, end=' ')

lst = [c for c in 'thingamabob']
for i in range(len(lst)):
    if i % 2 == 0:
       print(lst[i], end=' ')