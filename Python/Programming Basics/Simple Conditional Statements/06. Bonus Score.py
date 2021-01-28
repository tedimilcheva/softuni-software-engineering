num = int(input())
bonus = 0

if num <= 100:
    bonus = 5
    
elif 1000 >= num > 100:
    bonus = num * 20 / 100
    
else:
    bonus = num * 10 / 100

if num % 2 == 0:
    bonus = bonus + 1
    
elif num % 5 == 0:
    bonus = bonus + 2

print(bonus)
print(bonus + num)
