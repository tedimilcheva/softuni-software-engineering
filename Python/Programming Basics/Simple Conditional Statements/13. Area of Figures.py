import math

figure = input()
result = 'Invalid Result!'
a = float(input())

if figure == 'square':
    result = str('%.3f' % (a * a))
elif figure == 'rectangle':
    b = float(input())
    result = str('%.3f' % (a * b))
elif figure == 'circle':
    result = str('%.3f' % (math.pi * a * a))
elif figure == 'triangle':
    h = float(input())
    result = str('%.3f' % (a * h / 2))

print(result)
