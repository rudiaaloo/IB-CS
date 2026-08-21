# p(4) = 2 + 2(2) = 6 
# p(11) = 2 + w = int(input("pls give weight w of ure package posting p "))
if w <= 2:
    p = 3
elif w > 2 and w <= 5:
    p = p + 2*w 
elif w > 5: 
    p = p + 3*w 
