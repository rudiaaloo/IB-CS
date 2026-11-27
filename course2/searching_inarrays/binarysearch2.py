def bin_search(key, array): 
    lo = 0
    hi = len(array) -1 
    while lo <= hi: 
        mid = (lo + hi) // 2
        val = array[mid]
        if key == val: 
            return True 
        elif key < val: 
            hi = mid - 1 
        else: #key > val 
            low = mid + 1 
    return False 

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9] # constrain for this data i sthat it has to be sorted 
print(bin_search(5, lst)) # True



def bin_ser(key, array):
    low = 0 
    high = len(array)
    mid = int(low + high)/2 
    found = False 
    while not found: 
        if mid == key: 
            found = True
            return("found at", mid)
        elif mid < key:
            low = mid + 1 
        else:
            high = mid - 1 


print(bin_ser(7, lst))

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9] # constrain for this data i sthat it has to be sorted 
print(bin_search(5, lst))