amount = int(input())
numbers = []
odd_min, odd_max, even_min, even_max = 'No', 'No', 'No', 'No'
odd_sum, even_sum = 0, 0

for i in range(0, amount):
    numbers.append(float(input()))
    if i == 0:
        odd_min = numbers[i]
        odd_max = numbers[i]
    if i == 1:
        even_min, even_max = numbers[i], numbers[i]
    if i % 2 == 0:
        odd_sum = odd_sum + numbers[i]
        if numbers[i] < odd_min:
            odd_min = numbers[i]
        if numbers[i] > odd_max:
            odd_max = numbers[i]
    else:
        even_sum = even_sum + numbers[i]
        if numbers[i] < even_min:
            even_min = numbers[i]
        if numbers[i] > even_max:
            even_max = numbers[i]

print('OddSum=' + '%g' % odd_sum + ',')
if odd_min == 'No':
    print('OddMin=' + str(odd_min) + ',')
else:
    print('OddMin=' + ('%g' % odd_min) + ',')
if odd_max == 'No':
    print('OddMax=' + str(odd_max) + ',')
else:
    print('OddMax=' + '%g' % odd_max + ',')
print('EvenSum=' + '%g' % even_sum + ',')
if even_min == 'No':
    print('EvenMin=' + str(even_min) + ',')
else:
    print('EvenMin=' + '%g' % even_min + ',')
if even_max == 'No':
    print('EvenMax=' + str(even_max) + ',')
else:
    print('EvenMax=' + '%g' % even_max + ',')

