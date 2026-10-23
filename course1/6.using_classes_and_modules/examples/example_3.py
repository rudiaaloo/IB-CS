result = []

def find_all(s, sub):
    start = 0 #index where we start our search 
    while (m := s.find(sub, start)) != -1:
        result.append(m)
        start = m + 1 
    return result 

s = 'ababab' 
print(find_all('aba'))
#find substring and then once 1st index found, index + 1, 
#storing result in order to compare it = walrus 
#make empty list to store result