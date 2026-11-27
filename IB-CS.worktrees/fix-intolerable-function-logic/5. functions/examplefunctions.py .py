def abs_value(x):
    if x < 0:
        return -x
    else:
        return x 

for x in range(-5, 6):
    print(f"abs_value({x}) = {abs_value(x)}")