
n = int(input())

for d1 in range(1, 10):
    for d2 in range(1, 10):
        for d3 in range(1, 10):
            for d4 in range(1, 10):
                for d5 in range(1, 10):
                    for d6 in range(1, 10):
                        if d1 * d2 * d3 * d4 * d5 * d6 == n:
                            print(f'{d1}{d2}{d3}{d4}{d5}{d6}', end=' ')
