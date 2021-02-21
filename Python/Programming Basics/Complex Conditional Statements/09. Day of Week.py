s = int(input())

result = 'Error'
weekdays = ((1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'),
            (7, 'Sunday'))

for a, b in weekdays:
    if a == s:
        result = b

print(result)
