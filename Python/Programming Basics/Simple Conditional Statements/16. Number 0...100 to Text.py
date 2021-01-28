a = int(input())
twenties = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
            'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen','nineteen']
            
bigger = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'one hundred']
result = 'invalid number'

if 0 <= a <= 100:
    if a > 19:
        result = bigger[a // 10 - 2]
        if a % 10 != 0:
            result = result + ' ' + twenties[a % 10]
    else:
        result = twenties[a]

print(result)
