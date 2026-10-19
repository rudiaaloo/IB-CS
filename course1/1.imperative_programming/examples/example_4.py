n = int(input("Enter a number: "))
if n < 1:
    print('ERROR: invalid input.')
    exit()

a = n
res = 1

for x in range(2, n+1):
    res *= x

print(f'{a}! is {res}.')