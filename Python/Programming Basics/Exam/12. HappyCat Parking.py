days = int(input())
hours = int(input())
total = 0

for day in range(1, days + 1):
    day_result = 0
    for hour in range(1, hours + 1):
        if day % 2 == 0:
            if not hour % 2 == 0:
                day_result += 2.5
            else:
                day_result += 1
        else:
            if hour % 2 == 0:
                day_result += 1.25
            else:
                day_result += 1
    print(f'Day: {day} – {day_result:.2f} leva')
    total += day_result

print(f'Total: {total:.2f} leva')
