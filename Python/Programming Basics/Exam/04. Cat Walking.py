minutes_walking = int(input())
walking_times = int(input())
calories_intake = int(input())

calories_burned = minutes_walking * walking_times * 5
result = calories_intake / 2 - calories_burned

if calories_intake / 2 <= calories_burned:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {abs(calories_burned)}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {abs(calories_burned)}.')

