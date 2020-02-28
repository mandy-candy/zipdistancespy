import math

# format of input text file: PLZ;ORT;Kanton;Longitude;Latitude


# distance between two coordinates:
# longitude = x, latitude = y
# d = sqrt(pow(x1 - x2) + pow(y1 - y2))


# P1(5; 3) und P2(9; -4)

d = math.sqrt(pow(5 - 9, 2) + pow(3 - -4, 2))

print(d)
