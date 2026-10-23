N = 7 


for row in range(N): #value goes from 0 - (n-1), one option is to have 2nd variable for k an change that on the fly 
    for number in range(1, N + 1): #k+1 upperbound because it always take the last one - 1, not last one, 1 lower bound
        print(number, end=" ")
    N -= 1
    print() #number of rows depend on N, so changing it could be dettrimental to 
#change values of k, at certain level of indentation 
    