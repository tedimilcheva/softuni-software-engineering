x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

if (x1 <= x <= x2 and (y1 == y or y == y2)) or (y1 <= y <= y2 and (x1 == x or x2 == x)):
    print('Border')
else:
    print('Inside / Outside')
