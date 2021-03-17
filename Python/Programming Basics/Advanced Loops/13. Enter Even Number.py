even_number = int(input('Enter even number: '))

while not even_number % 2 == 0:
    print('The number is not even.')
    even_number = int(input('Enter even number: '))

print('Even number entered: ' + str(even_number))

