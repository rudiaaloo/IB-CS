a = int(input("gimme a nonnegative integer: "))
if a < 0:
    print(" u havent entered a nonnegative integer.")
else:
    print(f'{3**a}')

a = 3
res = 1
if (a == 0):
    print(1)
else:
    for x in range(a):
        res *= 3

print(res)
