n = int(input())
f0 = 1
f1 = 1
f2 = 0

if n <= 1:
    print(1)
else:
    for a in range(1, n):
        f2 = f0 + f1
        f0 = f1
        f1 = f2
    print(f2)

