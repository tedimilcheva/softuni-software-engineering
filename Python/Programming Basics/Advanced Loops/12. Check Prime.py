n = int(input())
result = 'prime'
a = 2
if n < 3:
    result = 'not prime'
else:
    while result == 'prime' and a < n:
        if n % a == 0:
            result = 'not prime'
        a += 1

print(result)
