n = int(input())

for row in range(n):
    for column in range(n):
        if column + row + 1 > n:
            print(str(2 * n - (row + column + 1)), end=' ')
        else:
            print(str(row + column + 1), end=' ')
    print('')
