highest_decrease = 0 



for t in range(101): 
    bacteria = t*(t - 20)*(t - 100) + 120000
    if bacteria > highest_decrease: 
        highest_decrease = bacteria
print(highest_decrease)

