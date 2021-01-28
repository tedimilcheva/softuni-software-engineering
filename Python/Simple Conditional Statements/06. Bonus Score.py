number = int(input())
bonus = 0

if number <= 100:
    bonus = 5
elif 1000 >= number > 100:
    bonus = number * 20 / 100
else:
    bonus = number * 10 / 100


if number % 2 == 0:
    bonus = bonus + 1
elif number % 5 == 0:
    bonus = bonus + 2

print(bonus)
print(bonus + number)
