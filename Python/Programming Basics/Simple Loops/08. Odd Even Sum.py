amount = int(input())

odd = 0
even = 0

for a in range(0, amount):
    if a % 2 == 0:
        odd += int(input())
    else:
        even += int(input())

if odd == even:
    print('Yes, sum = ' + str(odd))
else:
    print('No, diff = ' + str(abs(odd - even)))
