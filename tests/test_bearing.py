#!/usr/bin/python
# -*- coding: utf-8 -*-
from diblogeo import Geo

print('Calculate Bearing')
print('-' * 18)
print("\nDecimal Degrees:")
position = (55.3303636516, 10.4466164796, 11.2)
destination = (55.3706593849, 10.469825563, 9.34)
print(Geo(position).bearing(destination))

print("\nDegrees Minute Second:")
position = ("""55° 19' 49.30915" N""", """10° 26' 47.81933" E""", 11.2)
destination = ("""55° 22' 14.37379" N""", """10° 28' 11.37203" E""", 9.34)
print(Geo(position).bearing(destination))


print("\nUnits:")
bearing = Geo(position).bearing(destination)
units = ['deg', 'degrees', 'rad', 'radians']
for unit in units:
    print('%s %s'  %(getattr(bearing, unit), unit))

print("\nCalculation:")
bearing = Geo(position).bearing(destination)
print(bearing)
print(bearing + 5)
print(bearing + 5.3)
print(bearing + bearing)
print(bearing - bearing)
print(bearing * bearing)
print(bearing * bearing + 5)
print(bearing / bearing)
