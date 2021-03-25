age = int(input())
price = float(input())
toy_price = int(input())
total = 0
toys = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        total += i / 2 * 10 - 1
    else:
        total += toy_price
        toys += 1

if total >= price:
    print('Yes! ' + '%.2f' % (total-price))
else:
    print('No! ' + '%.2f' % (price-total))
