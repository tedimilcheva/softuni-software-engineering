sleeve_size = float(input())
front_size = float(input())
fabric = input()
tie = input()

Linen = 15
Cotton = 12
Denim = 20
Twill = 16
Flannel = 11

cost_in_meters = (sleeve_size + front_size) * 2 * 1.1 / 100
price = cost_in_meters * globals()[fabric] + 10
if tie == 'Yes':
    price *= 1.2

print(f'The price of the shirt is: {price:.2f}lv.')
