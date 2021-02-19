product = input()
day = input()
amount = float(input())
result = 'error'
price = [('banana', 2.50, 2.70), ('apple', 1.20, 1.25), ('orange', 0.85, 0.90), ('grapefruit', 1.45, 1.60),
         ('kiwi', 2.70, 3.00), ('pineapple', 5.50, 5.60), ('grapes', 3.85, 4.20)]
result = 'error'

for a, b, c, in price:
    if day in ('Sunday', 'Saturday'):
        if product == a:
            result = '{0:.2f}'.format(amount * c)
    elif day in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'):
        if product == a:
            result = '{0:.2f}'.format(amount * b)

print(result)
