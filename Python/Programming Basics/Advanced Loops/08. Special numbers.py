n = int(input())

for number in range(1111, 10000):
    ones = number % 10
    tens = ones % 10
    hundreds = tens % 10
    thousands = hundreds % 10
    if ones > 0 and tens > 0 and hundreds > 0 and thousands > 0:
        if n % ones == n % tens == n % hundreds == n % thousands == 0:
            print(str(number), end=' ')
