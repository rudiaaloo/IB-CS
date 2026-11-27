numbers = [3,9,7,4]
key = 7 
position = -1 
for i in range (0, len(numbers)):
    if key == numbers[i]:
        posiiton = i 
        if position != -1:
            print("element found on position", position)
        else:
            print("element not found")