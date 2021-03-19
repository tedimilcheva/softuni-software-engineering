fat_percentage = int(input())
protein_percentage = int(input())
carbohydrates_percentage = int(input())
total_calories = int(input())
water_percentage = int(input())

# Calculations
fat_weight = fat_percentage / 100 * total_calories / 9
protein_weight = protein_percentage / 100 * total_calories / 4
carbohydrates_weight = carbohydrates_percentage / 100 * total_calories / 4

total_weight = fat_weight + protein_weight + carbohydrates_weight
calories_per_gram = total_calories / total_weight

result = calories_per_gram * (1 - water_percentage / 100)

# Output
print(f'{result:0.4f}')
