action = int(input("enter an amount of points")) 
if action <= 17: 
   action = "hit"
elif action >= 21:
   action = "bust" 
else:
   action = "stay"
print(action) 