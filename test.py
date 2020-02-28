import math

# distance between two coordinates:
# longitude = x, latitude = y
# d = sqrt(pow(x1 - x2) + pow(y1 - y2))

# example:
# P1(5; 3) und P2(9; -4)
# d = math.sqrt(pow(5 - 9, 2) + pow(3 - -4, 2))
# print(d)

# format of input text file: PLZ;ORT;Kanton;Longitude;Latitude
# 9500;Wil SG;SG;9.043992;47.459015

list = [
    {
    "zip": "9500",
    "city": "Wil",
    "canton": "SG",
    "longitude": 9.043992,
    "latitude": 47.459015
    },
    {
    "zip": "2556",
    "city": "Schwadernau",
    "canton": "BE",
    "longitude": 7.314355,
    "latitude": 47.121929
    } ]

# print(list)
# print(list[0]["zip"])
# print(list[0]["city"])
