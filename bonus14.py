from bonus.converters14 import convert
from bonus.parsers14 import parse

feet_inches = input('enter feet and inches: ')

parsed = parse(feet_inches)
print(convert(parsed['feet'], parsed['inches']))
