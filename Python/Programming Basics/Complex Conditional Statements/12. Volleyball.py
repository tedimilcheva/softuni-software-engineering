import math

year = input()
p = int(input())
h = int(input())

result = 48.00 - h

saturday_games = result * 3 / 4
weekend_games = p * 2 / 3
result = saturday_games + h + weekend_games
if year == 'leap':
    result = result * 1.15

print(math.floor(result))

