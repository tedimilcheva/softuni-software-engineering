import math

#input
area = int(input())
grape_weight_per_meter = float(input())
target_amount_of_wine = int(input())
workers = int(input())

#calculations
harvested_grape = area * grape_weight_per_meter
grape_for_wine = harvested_grape * 0.4
generated_wine = grape_for_wine / 2.5
bonus_wine = generated_wine - target_amount_of_wine

#output
if generated_wine >= target_amount_of_wine:
    print(f'Good harvest this year! Total wine: {math.floor(generated_wine)} liters.')
    print(f'{math.ceil(bonus_wine)} liters left -> {math.ceil(bonus_wine / workers)} liters per person.')
else:
    print(f'It will be a tough winter! More {math.floor(target_amount_of_wine - generated_wine)} liters wine needed.')

