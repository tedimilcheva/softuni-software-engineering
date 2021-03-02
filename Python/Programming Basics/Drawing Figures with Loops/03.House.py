n = int(input())

if n % 2 == 0:
    stars = 2
else:
    stars = 1

for row in range(1, (n // 2) + (n % 2) + 1):
    print('-' * ((n - stars) // 2) + '*' * stars + '-' * ((n - stars) // 2))
    stars += 2

for row in range(1, (n // 2) + 1):
    print('|' + (n - 2) * '*' + '|')
