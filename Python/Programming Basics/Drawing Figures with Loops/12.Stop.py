n = int(input())
wide = 4 * n + 3

for row in range(0, n + 1):
    if row == 0:
        print((n - row + 1) * '.' + (2 * (n - row) + 1) * '_' + (n - row + 1) * '.')
    else:
        print((n - row + 1) * '.' + '//' + (2 * (n + row) - 3) * '_' + '\\\\' + (n - row + 1) * '.')

print('//' + (wide - 9)//2 * '_' + 'STOP!' + (wide - 9)//2 * '_' + '\\\\')

for row in range(n, 0, -1):
    print((n - row) * '.' + '\\\\' + (2 * (n + row) - 1) * '_' + '//' + (n - row) * '.')
