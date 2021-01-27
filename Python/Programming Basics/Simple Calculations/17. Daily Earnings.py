workdays = float(input())
daily_tips = float(input())
exchange_rate = float(input())

salary = workdays * daily_tips

annual_income = salary * 12 + salary * 2.5
net_income = annual_income - annual_income * 25 / 100
result = net_income / 365 * exchange_rate

print('%.2f' % result)
