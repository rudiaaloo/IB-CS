class Point: 
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    def __str__(self):
        return f'({self.x}, {self.y})'

#for texts

import pathlib
file_path = pathlib.Path("pp") / "points.txt"

#write for text
points_written = [Point(x, x**2) for x in range (20)]
f = open(file_path, "w")
for p in points_written: print(p.x, p.y, file= f)
f.close 

#read for text
f = open(file_path)
points_read = []
for line in f: 
    [x, y] = [int(word) for word in line.split()]
    points_read.append(Point(x, y))
f.close()
print(points_written[-1], points_read[-1])


#iterating 

import pathlib
f = open(pathlib.Path("pp") / "points.txt")
for line in f:
    line = line.removesuffix("\n")
    print(line)
f.close()


#to get rid of trailing newline
