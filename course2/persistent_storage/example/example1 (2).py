#serialization and deserialization 

class Point: 
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    def __str__(self):
        return f'({self.x}, {self.y})'

import pickle, pathlib 
file_path = pathlib.Path("points.ser")

points_written = [Point(x, x**2) for x in range(20)]
print(points_written[-1])

#for writing into binary
f = open(file_path, "wb")
pickle.dump(points_written, f) 
f.close()

#reading from binary
f = open(file_path, "rb")
points_read = pickle.load(f) #creating globa (?) variable 
f.close()
print(points_read[-1])

#HOLY POOP THIS IS SO COOL!!!
