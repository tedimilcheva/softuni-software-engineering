amount = float(input())
fr = input()
to = input()

USD = 1.79549
EUR = 1.95583
GBP = 2.53405
BGN = 1

amount = amount * globals()[fr] / globals()[to]
print(str(round(amount, 2)) + ' ' + to)
