import math

#input
needed_hours = int(input())
days_available = int(input())
extra_workers = int(input())


extra_hours = extra_workers * 2 * days_available
days_available *= 0.9
hours_available = days_available * 8
total_hours = math.floor(extra_hours + hours_available)
calculated_hours = total_hours - needed_hours


if calculated_hours >= 0:
    print(f'Yes!{calculated_hours} hours left.')
else:
    print(f'Not enough time!{abs(calculated_hours)} hours needed.')
