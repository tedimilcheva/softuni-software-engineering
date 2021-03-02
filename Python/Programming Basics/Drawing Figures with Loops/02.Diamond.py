n = int(input())
is_even = n % 2 == 0

leftRight = (n - 1) // 2

for row in range(0, n // 2 + n % 2):
    if is_even:
        print('-' * leftRight + '*' + row * '-', end='')
        print('-' * row + '*' + leftRight * '-')
    else:
        print('-' * leftRight + '*' + (row * 2 - 1) * '-', end='')
        if row == 0:
            print(leftRight * '-')
        else:
            print('*' + leftRight * '-')
    leftRight -= 1

leftRight = 1

for row in range(n // 2 + n % 2 - 2, -1, -1):
    if is_even:
        print('-' * leftRight + '*' + row * '-', end='')
        print('-' * row + '*' + leftRight * '-')
    else:
        print('-' * leftRight + '*' + (row * 2 - 1) * '-', end='')
        if row == 0:
            print(leftRight * '-')
        else:
            print('*' + leftRight * '-')
    leftRight += 1
