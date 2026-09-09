#walrus operator 
day = int(input('enter a day of the week (1-7): '))

#you would have to ask again, if not fo rthe wlarus operator, but with it you can do it in one line
while day := int(input('enter a day of the week (1-7): '))  #while input nonsense 
    print("invalid input, try again")

while not (1 <= (day := int(input('enter a day of the week (1-7): '))) <= 7): 
        print("pls provide valid day of the week") 

while (vacation := input("are you on vacation? (y/n)")) != 'yes' and vacation != 'no':
      pass 

print(vacation == 'yes' or day > 5)

        