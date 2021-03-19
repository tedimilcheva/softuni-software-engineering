cat_amount = int(input())

for cat in range(cat_amount):
    first_name = input()
    family_name = input()
    birth_year = int(input())
    print(str(birth_year) + str(ord(first_name[0])) + str(ord(family_name[0])) + str(cat + 1))
