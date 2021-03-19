breed = input()
sex = input()
is_breed_exist = False

breeds = (('British Shorthair', 13, 14),
          ('Siamese', 15, 16),
          ('Persian', 14, 15),
          ('Ragdoll', 16, 17),
          ('American Shorthair', 12, 13),
          ('Siberian', 11, 12))

for b in breeds:
    if b[0] == breed:
        is_breed_exist = True
        if sex == 'm':
            result = b[1] * 12 / 6
            print(f'{result:.0f} cat months')
        else:
            result = b[2] * 12 / 6
            print(f'{result:.0f} cat months')

if not is_breed_exist:
    print(f'{breed} is invalid cat!')
