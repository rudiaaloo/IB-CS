smallest = 0  ##idea is you keep track of the smallest number you have seen so far and compare it to the next number in the list. If the next number is smaller than the smallest number you have seen so far, you update the smallest number to be that next number.
largest = 0  ##have appropriate initial value
for n in range(51): 
    value = n*(n - 30)*(n - 50)
    if value < smallest: 
        smallest = value 
    if value > largest: 
        largest = value 
print(smallest, largest) 