food_amount = int(input()) * 1000
stop = input()

while not stop == 'Adopted':
    food_amount -= int(stop)
    stop = input()

if food_amount < 0:
    print(f'Food is not enough. You need {abs(food_amount)} grams more.')
else:
    print(f'Food is enough! Leftovers: {abs(food_amount)} grams.')
