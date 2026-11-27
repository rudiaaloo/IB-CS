def binary_search(key, array):
    low = 0 
    high = len(array) - 1
    mid = (low + high) // 2 
    while low <= high:
        if array[mid] == key:
            return(mid)
            break 
        elif array[mid]  < key: 
            low = mid + 1
        else: 
            high = mid - 1
    return False 
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9] # constrain for this data i sthat it has to be sorted 
print(binary_search(5, lst)) # True