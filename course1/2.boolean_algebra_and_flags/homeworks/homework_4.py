smallest = 1
found = False
a = int(input("enter an integer"))
b = int(input("enter an integer"))

while (not found):
    if (smallest % a == 0) and (smallest % b == 0):
        found = True 

    else: 
     smallest += 1 

print(smallest)
    
#this is basically finding LCM