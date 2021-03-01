
h = int(input())
x = int(input())
y = int(input())

result = 'Outside'

# Base, left vertical, left horizontal, middle left etc.

if (3*h >= x >= 0 == y) or (x == 0 <= y <= h) or (0 <= x <= h == y) or (x == h <= y <= 4*h) or \
        (h <= x <= 2*h and y == 4*h) or (x == 2*h and h <= y <= 4*h) or (2*h <= x <= 3*h and y == h) or \
        (x == 3*h and 0 <= y <= h):
    result = 'Border'
elif (0 < x < 3*h and 0 < y < h) or (h < x < 2*h and 0 < y < 4*h):
    result = 'Inside'

print(result)
