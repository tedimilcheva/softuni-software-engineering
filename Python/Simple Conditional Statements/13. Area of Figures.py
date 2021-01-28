import math

figure = input()
output = 'Invalid Result!'
a = float(input())

if figure == 'square':
    output = str('%.3f' % (a * a))
    
elif figure == 'rectangle':
    b = float(input())
    output = str('%.3f' % (a * b))
    
elif figure == 'circle':
    output = str('%.3f' % (math.pi * a * a))
    
elif figure == 'triangle':
    h = float(input())
    output = str('%.3f' % (a * h / 2))

print(output)
