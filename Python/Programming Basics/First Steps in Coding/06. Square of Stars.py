n = int(input())
for i in range(0, n):
    result = ""
    for y in range(0, n):
        if i == 0 or i == n-1:
            result = result + "*"
        else:
            if y == 0 or y == n - 1:
                result = result + "*"
            else:
                result = result + " "
    print(result)
