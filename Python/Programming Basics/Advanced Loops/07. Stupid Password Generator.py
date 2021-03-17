n = int(input())
el = int(input())

for number1 in range(1, n+1):
    for number2 in range(1, n+1):
        for char1 in range(ord('a'), 97 + el):
            for char2 in range(ord('a'), 97 + el):
                for number3 in range(1, n+1):
                    if number3 > number1 and number3 > number2:
                        print(str(number1) + str(number2) + chr(char1) + chr(char2) + str(number3), end=' ')
