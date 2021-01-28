vacation_time = int(input())

total_amount_of_time = 365
play_per_day_when_work = 63
play_per_day_when_vacation = 127
total_work_time = total_amount_of_time - vacation_time
total_play_time = total_work_time * play_per_day_when_work + \
                  vacation_time * play_per_day_when_vacation
diff = 30000 - total_play_time

hours = abs(diff) // 60
minutes = abs(diff) % 60

if total_play_time < 30000:
    print('Tom sleeps well')
    print(f'{abs(hours)} hours and {abs(minutes)} minutes less for play')
    
else:
    print('Tom will run away')
    print(f'{abs(hours)} hours and {abs(minutes)} minutes more for play')
