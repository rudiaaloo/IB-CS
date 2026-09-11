nonnegative_integer = int(input("pls enter a nongetaive integer: "))
lst = []
lst.append(nonnegative_integer) 
print(lst)
while (v := int(input("pls enter a nongetaive integer: "))) >= 0: #u could do without the variable but wlarus saves a whole line 
  i = 0 
  while i < len(lst) and lst[i] < v: #boundary test if u are still within the list bounds
    i += 1
  lst.insert (i, v) #if v < 0:
       #there is a while so no need to put the if 
 print(lst)

#didnt need extra rules for going to begining, or null list 1,2,4 HW 