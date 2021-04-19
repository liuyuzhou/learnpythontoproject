class Fib(object):
    def __init__(self):
        # 初始化两个计数器a、b
        self.a, self.b = 0, 1 

    def __iter__(self):
        # 实例本身就是迭代对象，故返回自己
        return self 

    def __next__(self):
        # 计算下一个值
        self.a, self.b = self.b, self.a + self.b
        # 退出循环的条件
        if self.a > 100000: 
            raise StopIteration()
        # 返回下一个值
        return self.a 


for n in Fib():
    print(n)
