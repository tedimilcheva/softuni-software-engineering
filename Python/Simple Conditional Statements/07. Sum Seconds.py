t_1 = int(input())
t_2 = int(input())
t_3 = int(input())
sum_time = t_1 + t_2 + t_3

minutes = sum_time // 60
seconds = sum_time % 60

print(str(minutes) + ':' + '%02d' % seconds)
