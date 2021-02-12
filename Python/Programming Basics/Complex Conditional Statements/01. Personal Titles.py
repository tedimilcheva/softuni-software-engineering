age = float(input())
sex = input()
result = ''
if age < 16:
    if sex.lower() == 'm':
        result = 'Master'
    else:
        result = 'Miss'
else:
    if sex.lower() == 'f':
        result = 'Ms.'
    else:
        result = 'Mr.'

print(result)
