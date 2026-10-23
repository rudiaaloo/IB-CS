numbers = [1, 1, 2, 3, 4]
#dont call i tlist bcoz list is a function to make a list 
for i in numbers:
    for j in numbers:
        if i == j:
            print(i) 
#this is a nested for loop and has O(n^2) 
#if there was a million then million x million and also arbitrary coefficient 
#arbitrary coefficient basically means time taken to run that n, and this "time" is basically CPU cycles 
# e.g sin(x) x 3 as comapred to O(1)
# you usually drop the coefficient because often you compare o(1) to like o(n), insetad of like o(1) to o(1)
# log of n building binary tree 

        
