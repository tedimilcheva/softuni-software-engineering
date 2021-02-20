
town = input()
s = float(input())
result = 'error'
discounts = [('Sofia', 5, 7, 8, 12), ('Varna', 4.5, 7.5, 10, 13), ('Plovdiv', 5.5, 8, 12, 14.5)]

for a, b, c, d, e in discounts:
    if a == town:
        if 0 <= s <= 500:
            result = '{0:.2f}'.format(s * b / 100)
        if 500 < s <= 1000:
            result = '{0:.2f}'.format(s * c / 100)
        if 1000 < s <= 10000:
            result = '{0:.2f}'.format(s * d / 100)
        if s > 10000:
            result = '{0:.2f}'.format(s * e / 100)

print(result)
