year = int(input("pls select a year:"))

leap = False #not a no

if year % 4 == 0: 
    leap = True 
elif year % 100 == 0:
    leap = False
elif year % 400 == 0:
    leap = True
else: 
    print("you havent entered a leap year")

print(f"{year} is a leap year: {leap}")

print(year % 4 == 0 and (not (year % 100 == 0) or year % 400 == 0))

#and comes before or 