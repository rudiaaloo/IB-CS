n = int(input("Enter a number: "))
smallest = 0 
largest = 0 
while n >= 0 and n <= 50:
    value = (n*(n - 30)*(n-50))
    if value < smallest:
        smallest = value
    if value > largest:
        largest = value 
print(f'Value: {value}, Smallest: {smallest}, Largest: {largest}')