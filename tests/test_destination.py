#!/usr/bin/python
# -*- coding: utf-8 -*-
from diblogeo import Geo

print('Project destination')
print('-' * 20)
print("\nDecimal Degrees:")
position = (55.3303636516, 10.4466164796, 11.2)
print(Geo(position).destination(32.3, 3.4))

print("\nDegrees Minute Second:")
position = ("""55° 19' 49.30915" N""", """10° 26' 47.81933" E""", 11.2)
print(Geo(position).destination(32.3, 3.4))


print("\nInput units:")
point = Geo(position)
units = ['km', 'kilometers', 'm', 'meters', 'cm', 'mi', 'miles', 'ft', 'feet', 'nautical', 'nmi', 'nm']
for unit in units:
    print("%11s: %s" %(unit, point.destination(32.3, **{unit: 3.4})))

print("\n__len__:")
print(len(Geo(position).destination(32.3, 3.4)))

print("\n__iter__:")
for coords in Geo(position).destination(32.3, 3.4):
    print(coords)

print("\n__getitem__:")
destination = Geo(position).destination(32.3, 3.4)
print(destination[0])
print(destination[1])
print(destination[2])

print("\nOther Output Options:")
destination = Geo(position).destination(32.3, 3.4)
options = ['dd', 'DD', 'dms', 'DMS', 'lat', 'latitude', 'lon', 'longitude', 'alt', 'altitude', 'elevation']
for option in options:
    print("%10s: %s" %(option, getattr(destination, option)))
