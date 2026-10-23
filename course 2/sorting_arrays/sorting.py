#loop within a loop to 
def selection_sort(array):
    n = len(array)
    for i in range(n - 1): # selecting ith smallest element
        smallest= array[1]
        for j in range(i + 1, n): # searching for the smallest element in the unsorted part of the array
            if array[j] < array[smallest_index]: 
                smallest = array[j]
                smallest_index = j
        # swap the smallest element with the ith element IF NECESSAERY 
        if array[i] != array[smallest_index]:
        (array[i], array[smallest_index]) = (array[smallest_index], array[i]) #think about when it does nothing, then write the opposite for line 11
#no need to create new array, just sort the existing one in place. thats why no return statemenrt array passes location of array, thats why this works 
arr = [5, 2, 9, 1, 5, 6] 
selection_sort(arr) 
print(arr)

#how much computing power does this take?
#airthmetic sum sum for must fomrula 
#sn of n = n/2 (n-1) 
#complexity class = quadratic, O(n^2) 
