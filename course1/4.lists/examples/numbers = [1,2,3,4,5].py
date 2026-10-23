numbers = [1,2,3,4,5]
smallest = numbers[0]
largest = numbers[0]

for i in range(len(numbers)):
    if numbers[i] < smallest:
        smallest = numbers[i]
    elif numbers[i] > largest: 
        largest = numbers[i]

'''
for i in range(len(numbers)):
    if numbers[i] < smallest:
            smallest = numbers[i]
'''

print(smallest, largest)
    
