nonnegative_integer = int(input("pls enter a nongetaive integer: "))
lst = []
lst.append(nonnegative_integer) 
print(lst)
while (v := int(input("pls enter a nongetaive integer: "))) >= 0: #u could do without the variable but wlarus saves a whole line 
   #if v < 0:
       #there is a while so no need to put the if 
    lst.append(v) 
    print(lst)