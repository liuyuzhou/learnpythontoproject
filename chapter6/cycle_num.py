# coding=UTF-8
import math

# 从1到10循环
for i in range(1, 10):
    # 从1到10循环
    for j in range(1, 10):
        # 数字i转化为字符串，重复j次
        num_str = str(i) * j
        # 数字字符串 num_str 转化为整数
        num_v = int(num_str)
        # 对整数 num_v 开平方
        cal_m = math.sqrt(num_v)
        # 开方后的结果 cal_m 根据点号（.）分割
        num_list = str(cal_m).split('.')
        # 分割后的小数位若大于 1，则不是 平方数
        if len(num_list[1]) > 1:
            print(f'{num_v} 不是平方数=================')
            continue

        print(f'-----------------{i} 是平方数.--------------')
