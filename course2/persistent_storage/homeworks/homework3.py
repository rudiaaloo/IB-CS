import pathlib
try: 
    file_path = pathlib.Path((input("please give file name in x.txt format where x = file")))
    with open(file_path, "r") as f:
        for line in f:
           read = f.read()
    print(read)
except Exception as e:
    print(Exception)
finally:
    print("file did not exist, or file is empty, or some text in file is not an int")


import pathlib
found = False 
while not found:
    try:
        file_path = pathlib.Path((input("please give file name in x.txt format where x = file")))
        with open(file_path, "r") as f:
                for line in f:
                   read = f.read()
                   if read 