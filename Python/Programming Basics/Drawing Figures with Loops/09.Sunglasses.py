n = int(input())

for row in range(0, n):
    if row == 0 or row == n - 1:
        print('*' * 2 * n + ' ' * n + '*' * 2 * n)
    else:
        if row == ((n - 1) // 2):
            print('*' + '/' * 2 * (n - 1) + '*' + '|' * n + '*' + '/' * 2 * (n - 1) + '*')
        else:
            print('*' + '/' * 2 * (n - 1) + '*' + ' ' * n + '*' + '/' * 2 * (n - 1) + '*')

