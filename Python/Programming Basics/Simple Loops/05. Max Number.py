amount = int(input())

result = int(input())

for i in range(1, amount):
    num = int(input())
    if num > result:
        result = num

print(result)
