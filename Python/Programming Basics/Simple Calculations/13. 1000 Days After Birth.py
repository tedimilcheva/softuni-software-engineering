from datetime import date, timedelta

day, month, year = input().split('-')
input_date = date(int(year), int(month), int(day))
date_format = '%d-%m-%Y'

result = input_date + timedelta(days=999)

print(result.strftime(date_format))
