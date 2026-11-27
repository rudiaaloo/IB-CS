#context manager
import pathlib 
file_path = pathlib.Path("pp") / ("points.txt")
with open(file_path) as f: 
    for line in f: 
        print(line)


#to use this for w or wb the code would change to: 


#to use this for r or rb the code would change to: 