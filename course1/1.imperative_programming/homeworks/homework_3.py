#1

n_1 = 10
while (n_1 < 38):
    print(n_1, end= ' ')
    n_1 += 3

print("\n")

#2 

n_2 = 1000

while(n_2 > 900):
    n_2 -= 2
    print(n_2, end= ' ') #in this case, we put print after the -= 2 because we want to print the value of 1000 it has been decremented by 2.

print("\n")

#3 

for i in range(1, 20):
    if (i % 2 == 0):
        print(-1, end= ' ')
    else:
        print(1, end= ' ')

print("\n")

#4 
for i in range(1, 61):
    if (i % 3 == 0):
        print(9, end= ' ')
    elif (i % 2 == 0):
        print(7, end= ' ')
    else:
        print(7, end= ' ')

print("\n")

#or 

for i in range(1, 61):
    if (i % 3 == 0):
        print(9, end= ' ')
    else:
        print(7, end= ' ')

print("\n")
