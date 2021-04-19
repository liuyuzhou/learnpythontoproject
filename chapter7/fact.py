def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(f'调用递归函数执行结果为：{fact(5)}')
