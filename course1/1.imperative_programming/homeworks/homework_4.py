points = int(input("Enter the number of points: "))
if points < 17:
    action = "hit"
elif points < 21:
    action = "stay"
else:
    action = "bust"
print("Action:", action)