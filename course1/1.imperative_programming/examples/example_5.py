#1. for x in range(9, 69, 4):
    #print(x, end=' ')  or use while loop n += 4

#for x in range(0, 13): --> reason for 0 is because 0^2 = 1 and thats what we need for further multiplication
    #print(3 * 2**x, end=' ') 

     #print(i, end=' ')
#every 4th integer is -1, otherwise normal 1-40 
for x in range (1, 41):
    if x % 4 == 0:
        print(-1, end=' ')
    else:
        print(x, end=' ')