#1. a. p(4) = 3 + 2(2) = 7 
#   b. p(w) = 3 + 2(w-2) = 3 + 2 * w - 4 = 2 * w - 1 
#2.  
#   a. p(w) = p(5) + (11-5)3 = 18 + 3 + 3(2) = 30 
#   b. p(w) = (w-5)*3 + P(5) = (w-5)*3 + 3 + (5-2)*2 = (w-5)*3 + 9 = 3 * w - 15 + 9 = 3 * w - 6

w = int(input("enter the weight w: "))
if (w <= 2):
    price = 3
elif (2 < w <= 5):
    price = 3 + 2*w - 1 
else: 
    price = 3 * w - 6

print(price)