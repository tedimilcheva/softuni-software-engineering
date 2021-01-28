hours = int(input())
minutes = int(input()) + 15

if minutes // 60 > 0:
    hours = hours + (minutes // 60)
    minutes = minutes % 60

hours = hours % 24

print(str(hours) + ':' + str('%02d' % minutes))
