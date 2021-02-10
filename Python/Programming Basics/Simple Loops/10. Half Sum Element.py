amount = int(input())
numbers = []
total = 0

for a in range(0, amount):
    numbers.append(int(input()))
    total = total + numbers[a]


biggest = numbers[0]
position = 0
for a in range(0, amount):
    if biggest < numbers[a]:
        biggest = numbers[a]
        position = a

half = total / 2
isExist = False

for a in range(0, amount):
    if half == numbers[a]:
        isExist = True

if isExist:
    print('Yes')
    print('Sum = ' + str(numbers[position]))
else:
    print('No')
    print('Diff = ' + str(abs(biggest - (total - biggest))))
