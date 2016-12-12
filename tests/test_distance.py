#!/usr/bin/python
# -*- coding: utf-8 -*-
from diblogeo import Geo

print('Measuring Distances')
print('-' * 19)
print("\nDecimal Degrees:")
position = (55.3303636516, 10.4466164796, 11.2)
destination = (55.3706593849, 10.469825563, 9.34)
print(Geo(position).distance(destination))

print("\nDegrees Minute Second:")
position = ("""55° 19' 49.30915" N""", """10° 26' 47.81933" E""", 11.2)
destination = ("""55° 22' 14.37379" N""", """10° 28' 11.37203" E""", 9.34)
print(Geo(position).distance(destination))

print("\nUnits:")
distance = Geo(position).distance(destination)
units = ['km', 'kilometers', 'm', 'meters', 'cm', 'mi', 'miles', 'ft', 'feet', 'nautical', 'nmi', 'nm']
for unit in units:
    print('%s %s'  %(getattr(distance, unit), unit))

print("\nCalculation:")
distance = Geo(position).distance(destination)
print(distance)
print(distance + 5)
print(distance + 5.3)
print(distance + distance)
print(distance - distance)
print(distance * distance)
print(distance * distance + 5)
print(distance / distance)
