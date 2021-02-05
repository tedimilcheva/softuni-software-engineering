n = int(input())
p = [0, 0, 0, 0, 0]

for i in range(0, n):
    tmp = int(input())
    if tmp < 200:
        p[0] += 1
    elif tmp < 400:
        p[1] += 1
    elif tmp < 600:
        p[2] += 1
    elif tmp < 800:
        p[3] += 1
    else:
        p[4] += 1

for a in p:
    print(round(a / n * 100, 2))
