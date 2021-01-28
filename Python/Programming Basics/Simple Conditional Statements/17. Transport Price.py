n = float(input())
when = str(input())
taxi_result = 0
result = 0

if when == 'day':
    taxi_result += 0.70 + 0.79 * n
    
else:
    taxi_result += 0.70 + 0.90 * n
    
bus_result = 0.09 * n
train_result = 0.06 * n

if n >= 100:
    result = train_result
if 20 <= n < 100:
    result = bus_result
if n < 20:
    result = taxi_result

print('%.2f' % result)
