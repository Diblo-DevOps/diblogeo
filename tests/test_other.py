#!/usr/bin/python
# -*- coding: utf-8 -*-
from diblogeo import Geo

print('Geo Class Test')
print('-' * 15)
print("\nDecimal Degrees:")
position = (55.3303636516, 10.4466164796, 11.2)
print(Geo(position))

print("\nDegrees Minute Second:")
position = ("""55° 19' 49.30915" N""", """10° 26' 47.81933" E""", 11.2)
print(Geo(position))

print("\n__len__:")
len(Geo(position).destination(32.3, 3.4))

print("\n__iter__:")
for coords in Geo(position).destination(32.3, 3.4):
    print(coords)

print("\n__getitem__:")
destination = Geo(position).destination(32.3, 3.4)
print(destination[0])
print(destination[1])
print(destination[2])

print("\nOther Output Options:")
point = Geo(position)
options = ['dd', 'DD', 'dms', 'DMS', 'lat', 'latitude', 'lon', 'longitude', 'alt', 'altitude', 'elevation']
for option in options:
    print("%10s: %s" %(option, getattr(point, option)))

print("\nNo Altitude Test")
print('-' * 17)
print("\nDecimal Degrees:")
position = (55.3303636516, 10.4466164796)
print(Geo(position))

print("\nDegrees Minute Second:")
position = ("""55° 19' 49.30915" N""", """10° 26' 47.81933" E""")
print(Geo(position))

print("\n__len__:")
print(len(Geo(position)))

print("\n__iter__:")
for coords in Geo(position):
    print(coords)

print("\n__getitem__:")
point = Geo(position)
print(point[0])
print(point[1])
print(point[2])

print("\nOther Output Options:")
point = Geo(position)
options = ['dd', 'DD', 'dms', 'DMS', 'lat', 'latitude', 'lon', 'longitude', 'alt', 'altitude', 'elevation']
for option in options:
    print("%10s: %s" %(option, getattr(point, option)))
