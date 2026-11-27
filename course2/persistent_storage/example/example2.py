#checking if file exists 
import pickle, pathlib 
file_path = pathlib.Path("points.ser")
if file_path.exists(): #remember its a func so its gonna have ()
    print("reading", file_path)
else:
    print("no file", file_path)

    #HOLY SHUCKS THIS IS ALSO SO FLIIPING COOL it was "data" / "data.ser" before BUT I CHANGED IT TO points.ser CUZ I REMEMBERED!!
    #now lemme try read it...

f = open(file_path, "rb")
points_read = pickle.load(f) #creating globa (?) variable 
f.close()
print(points_read[-1])