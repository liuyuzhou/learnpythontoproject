import time

start_time=time.time()
time_add=start_time + 10  			#不指明，加减的值指的是妙（s）
time_gap=time_add-start_time
print(f'计算得到的时间间隔为:{time_gap}秒')

start_time=time.time()
time_add=start_time + 0.1
time_gap=time_add-start_time
print(f'计算得到的时间间隔为:{1000 * time_gap}毫秒')

start_time=time.time()
time_add=start_time + 90
time_gap=time_add-start_time
print(f'计算得到的时间间隔为:{time_gap/60}分钟')

start_time=time.time()
time_add=start_time + 3600
time_gap=time_add-start_time
print(f'计算得到的时间间隔为:{time_gap/60/60}小时')
