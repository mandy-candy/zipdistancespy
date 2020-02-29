import math
import test_list

# format of input text file: PLZ;ORT;Kanton;Longitude;Latitude
# 9500;Wil SG;SG;9.043992;47.459015

masterLocation = [
    {
    "zip": "9500",
    "city": "Wil",
    "canton": "SG",
    "longitude": 9.043992,
    "latitude": 47.459015
    },
    {
    "zip": "6500",
    "city": "Bellinzona",
    "canton": "TI",
    "longitude": 9.02266750657928,
    "latitude": 46.1999320324997
    }
]

#print(masterLocation)
# access key in list
# print(list[0]["zip"])

# distance between two coordinates:
# longitude = x, latitude = y
# d = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

# example:
# P1(5; 3) und P2(9; -4)
# d = math.sqrt(pow(5 - 9, 2) + pow(3 - -4, 2))
# print(d)

for i in range(len(test_list.locations)):
    for j in range(len(masterLocation)):
        distance = math.sqrt(pow(masterLocation[j]["longitude"] - test_list.locations[i]["longitude"], 2) + pow(masterLocation[j]["latitude"] - test_list.locations[i]["latitude"], 2))
        print(masterLocation[j])
        test_list.locations[i]["distance"] = distance
        print(test_list.locations[i])
        #print(distance)
