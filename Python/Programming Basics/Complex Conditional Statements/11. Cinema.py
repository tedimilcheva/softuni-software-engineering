t = input()
lines = int(input())
columns = int(input())
result = 0

if t == 'Premiere':
    result = columns * lines * 12
elif t == 'Normal':
    result = columns * lines * 7.5
elif t == 'Discount':
    result = columns * lines * 5

print('{0:.2f} leva'.format(result))
