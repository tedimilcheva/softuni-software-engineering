budget = float(input())
category = input()
people = int(input())

if category == 'VIP':
    price = 499.99
else:
    price = 249.99

if 0 < people <= 4:
    budget = budget * 0.25
elif people <= 9:
    budget = budget * 0.40
elif people <= 24:
    budget = budget * 0.50
elif people <= 49:
    budget = budget * 0.60
else:
    budget = budget * 0.75

if budget >= price * people:
    print('Yes! You have {0:.2f} leva left.'.format(budget - price * people))
else:
    print('Not enough money! You need {0:.2f} leva.'.format(price * people - budget))

