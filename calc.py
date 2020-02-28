import math

# plz from switzerland 4120
# places for service 80

# result = math.factorial(4120)
# print(result)

plz = 4120
places = 80

for places in range(plz):
    result = places * plz
    places = places - 1

print(result)  