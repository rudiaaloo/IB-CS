#trying to write something following the pseudocode

#index = 0 
#found= false 
#while not found and index <N 
#if array[index]=KEY then 
#found = true 
#end if 
#index = index + 1 
#end loop 
#output loop



#i = 0 
#found = False 
#while not found: #while IT IS true that IT IS NOT found kep running, 
  #  if array[i] == key:
  #      found = True 
   # else: 
    #    i += 1 

#for loop 
def seq_search(array, key):
    for i in range(len(array)):
        if array[i] == key: 
         return (i)  
    else:
     return("not here")
    
array = [1, 2, 3, 4, 5]
key = 5

print(seq_search(array, key))