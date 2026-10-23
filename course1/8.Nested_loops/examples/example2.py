flights = ["AY664", "BA047", "AF110", "LH554", "AY181"]
airlines =  ["AY", "UA", "LH"]
print()

for a in airlines:
    print(f'(a):', end=" ")
    for f in flights: 
        if f.startswith(a):
            print(f, end=" ")
    