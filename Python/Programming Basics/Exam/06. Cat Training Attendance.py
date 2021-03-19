start_hour = int(input())
mark_hour = int(input())
mark_minutes = int(input())
day = input()

Monday = 0.6
Wednesday = 0.6
Friday = 0.6
Tuesday = 0.8
Thursday = 0.8
Saturday = 0.8
Sunday = 2

result = globals()[day]
mark = mark_hour * 60 + mark_minutes
start = start_hour * 60

if mark < start:
    result += 1.5
elif mark <= start + 30:
    result += 1
elif mark <= start + 240:
    result += 0.5

print(f'{result:.2f}')
