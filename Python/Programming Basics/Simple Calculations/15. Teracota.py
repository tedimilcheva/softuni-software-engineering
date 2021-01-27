floor_lenght = float(input())
tile_wight = float(input())
tile_lenght = float(input())
bench_wight = float(input())
bench_lenght = float(input())

speed = 0.2

bench_area = bench_lenght * bench_wight
tile_area = (tile_wight * tile_lenght)
floor_area = floor_lenght * floor_lenght - bench_area

print("%.2f" % (floor_area/tile_area))
print("%.2f" % (floor_area/tile_area*speed))
