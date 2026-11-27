#exception handling 
class Point: 
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    def __str__(self):
        return f'({self.x}, {self.y})'


try: 
    import pathlib
    file_path = pathlib.Path("pp") / "points.txt"
    with open(file_path) as f:
        points_read = []
        for line in f: 
            [x,y] = [int(word) for word in line.split()]
            points_read.append(Point(x, y))
    print(points_read[-1])
except Exception as e: 
    print("exception:", e)  