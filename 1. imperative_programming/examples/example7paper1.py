s = int(input("please give the value of s:"))

n = 1 #n starts at 1 because we are looking for the first n that satisfies the condition, if we start at 0 we will always find a solution at n=0 which is not what we want
#boolean flag wether we have found the varibale we are lloking for, dormant condition flag raised when found 
found = False 
#why do we need to identify the false once an then again?
while found == False #one way to write it
   if n*(n+1)/2 > s:
       found = True 
    else:
       n += 1 
#while loop is natural because we hve no way of knowing when it stops 
print(n)

