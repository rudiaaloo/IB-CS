key_name = ["rudi", "veer", "mama"] 
room_value = [100, 101, 102]

#searching for a persons room 
search_name = "veer"

for i in range(len(key_name)):
    if key_name[i] == search_name:
        print(room_value[i]) 

