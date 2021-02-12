import sys
amount = int(input())
result = []

max_diff = 0

for i in range(0, amount):
    result.append(int(input()) + int(input()))
    if i > 0:
        if abs(result[i] - result[i - 1]) > max_diff:
            max_diff = abs(result[i] - result[i - 1])

if max_diff == 0:
    print('Yes, value=' + str(result[0]))
else:
    print('No, maxdiff=' + str(max_diff))
