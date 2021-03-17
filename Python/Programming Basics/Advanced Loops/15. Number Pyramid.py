limes = int(input())
count = 1
column = 2

for i in range(0, limes):
    if count == 0:
        print('')
        count = column
        column += 1
    print(str(i + 1), end=' ')
    count -= 1
