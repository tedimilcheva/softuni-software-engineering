num = float(input())

result = 'Invalid Speed Entrance!'

if 0 <= num <= 10:
    result = 'slow'
    
elif 10 < num <= 50:
    result = 'average'
    
elif 50 < num <= 150:
    result = 'fast'
    
elif 150 < num <= 1000:
    result = 'ultra fast'
    
elif 1000 < num:
    result = 'extremely fast'

print(result)
