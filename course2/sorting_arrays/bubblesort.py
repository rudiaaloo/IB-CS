def bubble_sort(array):
    n = len(array)
    ordered = False #it could be ordered ut we dont know, so we cannot garuntee 
    while not ordered: #we dont know how many times we need to loop, so we use while loop
        ordered = True 
        for i in range(n - 1): #n-2 is the correct index but n - 1 is the parameter
            if array[i] > array[i + 1]: #if the current element is greater than the next element, we need to swap them
                (array[i], array[i + 1]) = (array[i + 1], array[i]) #swap the elements
                ordered = False #we made a swap, so we cannot guarantee that the array is ordered

array = [5, 2, 9, 1, 5, 6] 
bubble_sort(array)
print(array) 
