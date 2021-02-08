amount = int(input())

result = sys.maxsize

for i in range(0, amount):
    tmp = int(input())
    if tmp < result:
        result = tmp

print(result)
