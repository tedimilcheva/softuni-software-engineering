product = input()
town = input()
amount = float(input())
result = 0

if town.lower() == 'sofia':
    if product.lower() == 'coffee':
        result = amount * 0.5
    if product.lower() == 'water':
        result = amount * 0.8
    if product.lower() == 'beer':
        result = amount * 1.2
    if product.lower() == 'sweets':
        result = amount * 1.45
    if product.lower() == 'peanuts':
        result = amount * 1.60
elif town.lower() == 'plovdiv':
    if product.lower() == 'coffee':
        result = amount * 0.4
    if product.lower() == 'water':
        result = amount * 0.7
    if product.lower() == 'beer':
        result = amount * 1.15
    if product.lower() == 'sweets':
        result = amount * 1.30
    if product.lower() == 'peanuts':
        result = amount * 1.50
elif town.lower() == 'varna':
    if product.lower() == 'coffee':
        result = amount * 0.45
    if product.lower() == 'water':
        result = amount * 0.7
    if product.lower() == 'beer':
        result = amount * 1.1
    if product.lower() == 'sweets':
        result = amount * 1.35
    if product.lower() == 'peanuts':
        result = amount * 1.55
print(result)
