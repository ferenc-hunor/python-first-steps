import math

a = 1
b = 2
c = 0

delta = b * b - 4 * a * c

if delta >= 0:
    x1 = (-1 * b + math.sqrt(delta)) / 2 * a
    x2 = (-1 * b - math.sqrt(delta)) / 2 * a
else:
    print('komplex!!!')
print('A megoldasok: %d %d' % (x1, x2))

print('A program indul')
number_of_the_boys = 0

if number_of_the_boys == 0:
    print('A szám == 0')
elif number_of_the_boys > 0:
    print('A szám nem pozitív')
elif number_of_the_boys < 0:
    print('A szám pozitiv')

print('A program befejeződött')
