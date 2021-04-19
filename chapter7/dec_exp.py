# coding=UTF-8
from functools import wraps
import time


def decorator(func):
    """
    装饰器函数
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数名：{func.__name__} 。执行时间花费： {end_time - start_time} s")
        return ret
    return wrapper


@decorator
def test_dec():
    """
    装饰器使用示例
    :return:
    """
    for i in range(3):
        time.sleep(1)


if __name__ == "__main__":
    test_dec()
