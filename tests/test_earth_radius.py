#!/usr/bin/python
# -*- coding: utf-8 -*-
from diblogeo import calc_earth_radius

print('Calculate Earth\'s Radius')
print('-' * 26)
print("\nDecimal Degrees:")
position = (55.3303636516, 10.4466164796, 11.2)
print(calc_earth_radius(position))

print("\nDegrees Minute Second:")
position = ("""55° 19' 49.30915" N""", """10° 26' 47.81933" E""", 11.2)
print(calc_earth_radius(position))

print("\nUnits:")
earth_radius = calc_earth_radius(position)
units = ['km', 'kilometers', 'm', 'meters', 'cm', 'mi', 'miles', 'ft', 'feet', 'nautical', 'nmi', 'nm']
for unit in units:
    print('%s %s'  %(getattr(earth_radius, unit), unit))

print("\nCalculation:")
earth_radius = calc_earth_radius(position)
print(earth_radius)
print(earth_radius + 5)
print(earth_radius + 5.3)
print(earth_radius + earth_radius)
print(earth_radius - earth_radius)
print(earth_radius * earth_radius)
print(earth_radius * earth_radius + 5)
print(earth_radius / earth_radius)
