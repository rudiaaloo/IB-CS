import pathlib 
arr = [4, 2, 3, "rudi", 5]
file_path = pathlib.Path("text.txt")
#f = open(file_path, "w")
#for i in arr: 
   # print(i, end=" ", file=f)
#f.close()

#1 

#f = open(file_path, "r")
#read = []
#for line in f: 
    #read.append(line)
#f.close()
#print(read)

#2

#context manager 
  #1 write
with open(file_path, "w") as f:
    for i in arr: 
        print(i, end=" ", file=f)

#2 read 
read = []
with open(file_path, "r") as f:
   for line in f: 
      read.append(line)
print(read)


#with open(file_path, "r") as f:
   #text = f.read()
   #print(text)
