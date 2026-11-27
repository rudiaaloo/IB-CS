def read_words_from_url(url):
    import requests


    response = requests.get(url, stream=True)
    words = [line.decode('utf-8').strip() for line in response.iter_lines()]

    return words 

words = read_words_from_url("https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words_alpha.txt")
words = [w for w in words if w != ""]   # remove the blank entries
print(words[-10:]) 


import time

def time_search(algo, key, array, repeats):
    start = time.process_time()
    for _ in range(repeats):
        algo(key, array)
    end = time.process_time()
    return (end - start) / repeats   # average time for ONE search

def sequential_search(arrayss, keyss):
    i = 0 
    found = False
    while not found: 
        if arrayss[i] == keyss:
            found = True 
            print(i)          
        else: 
            i += 1

gang = [1, 2, 3, 4, 5]
keya = 8 
sequential_search(gang, keya)