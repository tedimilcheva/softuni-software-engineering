bed_price = float(input())
lavatory_price = float(input())

monthly_expenses = (
        lavatory_price + lavatory_price * 1.25 + lavatory_price * 1.25 * 0.5 + lavatory_price * 1.25 * 0.5 * 1.1)
result = bed_price + monthly_expenses * 12 + 12 * monthly_expenses * 0.05

print(f'{result:.2f} lv.')
