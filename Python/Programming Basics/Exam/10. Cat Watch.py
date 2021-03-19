
n = int(input())

for a in range(n - 2):
    print(n * ' ' + '||' + (n - 2) * '_' + '||')

print((n - 1) * ' ' + '//' + n * ' ' + '\\\\')

for a in range(1, n - 3):
    if n % 2 == 0:
        if a == (n - 4) // 2:
            print((n - 2) * ' ' + '||' + (n + 2) * ' ' + '||' + ']')
        else:
            print((n - 2) * ' ' + '||' + (n + 2) * ' ' + '||')
    else:
        if a == (n - 3) // 2:
            print((n - 2) * ' ' + '||' + (n + 2) * ' ' + '||' + ']')
        else:
            print((n - 2) * ' ' + '||' + (n + 2) * ' ' + '||')

print((n - 1) * ' ' + '\\\\' + n * ' ' + '//')

for a in range(n - 2):
    print(n * ' ' + '||' + (n - 2) * '_' + '||')
