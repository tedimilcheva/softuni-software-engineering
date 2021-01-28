input_amount = float(input())
input_type = input()
result_type = input()

m = float(1)
mm = 1 / 1000
cm = 1 / 100
mi = 1 / 0.000621371192
inch = 1 / 39.3700787
km = 1 / 0.001
ft = 1 / 3.2808399
yd = 1 / 1.0936133

result = 0

if result_type == 'm':
    if input_type == 'm':
        result = input_amount / m * m
    elif input_type == 'mm':
        result = input_amount / m * mm
    elif input_type == 'cm':
        result = input_amount / m * cm
    elif input_type == 'mi':
        result = input_amount / m * mi
    elif input_type == 'in':
        result = input_amount / m * inch
    elif input_type == 'km':
        result = input_amount / m * km
    elif input_type == 'ft':
        result = input_amount / m * ft
    elif input_type == 'yd':
        result = input_amount / m * yd

if result_type == 'mm':
    if input_type == 'm':
        result = input_amount / mm * m
    elif input_type == 'mm':
        result = input_amount / mm * mm
    elif input_type == 'cm':
        result = input_amount / mm * cm
    elif input_type == 'mi':
        result = input_amount / mm * mi
    elif input_type == 'in':
        result = input_amount / mm * inch
    elif input_type == 'km':
        result = input_amount / mm * km
    elif input_type == 'ft':
        result = input_amount / mm * ft
    elif input_type == 'yd':
        result = input_amount / mm * yd

if result_type == 'cm':
    if input_type == 'm':
        result = input_amount / cm * m
    elif input_type == 'mm':
        result = input_amount / cm * mm
    elif input_type == 'cm':
        result = input_amount / cm * cm
    elif input_type == 'mi':
        result = input_amount / cm * mi
    elif input_type == 'in':
        result = input_amount / cm * inch
    elif input_type == 'km':
        result = input_amount / cm * km
    elif input_type == 'ft':
        result = input_amount / cm * ft
    elif input_type == 'yd':
        result = input_amount / cm * yd

if result_type == 'mi':
    if input_type == 'm':
        result = input_amount / mi * m
    elif input_type == 'mm':
        result = input_amount / mi * mm
    elif input_type == 'cm':
        result = input_amount / mi * cm
    elif input_type == 'mi':
        result = input_amount / mi * mi
    elif input_type == 'in':
        result = input_amount / mi * inch
    elif input_type == 'km':
        result = input_amount / mi * km
    elif input_type == 'ft':
        result = input_amount / mi * ft
    elif input_type == 'yd':
        result = input_amount / mi * yd

if result_type == 'in':
    if input_type == 'm':
        result = input_amount / inch * m
    elif input_type == 'mm':
        result = input_amount / inch * mm
    elif input_type == 'cm':
        result = input_amount / inch * cm
    elif input_type == 'mi':
        result = input_amount / inch * mi
    elif input_type == 'in':
        result = input_amount / inch * inch
    elif input_type == 'km':
        result = input_amount / inch * km
    elif input_type == 'ft':
        result = input_amount / inch * ft
    elif input_type == 'yd':
        result = input_amount / inch * yd

if result_type == 'km':
    if input_type == 'm':
        result = input_amount / km * m
    elif input_type == 'mm':
        result = input_amount / km * mm
    elif input_type == 'cm':
        result = input_amount / km * cm
    elif input_type == 'mi':
        result = input_amount / km * mi
    elif input_type == 'in':
        result = input_amount / km * inch
    elif input_type == 'km':
        result = input_amount / km * km
    elif input_type == 'ft':
        result = input_amount / km * ft
    elif input_type == 'yd':
        result = input_amount / km * yd

if result_type == 'ft':
    if input_type == 'm':
        result = input_amount / ft * m
    elif input_type == 'mm':
        result = input_amount / ft * mm
    elif input_type == 'cm':
        result = input_amount / ft * cm
    elif input_type == 'mi':
        result = input_amount / ft * mi
    elif input_type == 'in':
        result = input_amount / ft * inch
    elif input_type == 'km':
        result = input_amount / ft * km
    elif input_type == 'ft':
        result = input_amount / ft * ft
    elif input_type == 'yd':
        result = input_amount / ft * yd

if result_type == 'yd':
    if input_type == 'm':
        result = input_amount / yd * m
    elif input_type == 'mm':
        result = input_amount / yd * mm
    elif input_type == 'cm':
        result = input_amount / yd * cm
    elif input_type == 'mi':
        result = input_amount / yd * mi
    elif input_type == 'in':
        result = input_amount / yd * inch
    elif input_type == 'km':
        result = input_amount / yd * km
    elif input_type == 'ft':
        result = input_amount / yd * ft
    elif input_type == 'yd':
        result = input_amount / yd * yd

if result == 0:
        print('Not a valid input')
else:
    print(f'{result} {result_type}')

