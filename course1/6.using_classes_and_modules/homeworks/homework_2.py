def date_of_birth(ssn):
    day = int(ssn[:2]) #we put int() so that it makes str --> int 
    month = int(ssn[2:4])
    year = int(ssn[4:6])  
    c = ssn[6]
    
    if c == '+': 
        year += 1800
    elif c == '-':
        year += 1900
    else:
        year += 2000
    
    return year, month, day


print(date_of_birth('140589+abcd')) 