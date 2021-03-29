
import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numSwaps = 0

for i in range(n):
    current_swaps = 0
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            current_swaps += 1
    if current_swaps == 0:
        break
    numSwaps += current_swaps

print(f'Array is sorted in {numSwaps} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[-1]}')