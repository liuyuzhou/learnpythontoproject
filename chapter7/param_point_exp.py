def fun(a, b, /, c, d, *, e, f):
    print(f'{a=}, {b=}, {c=}, {d=}, {e=}, {f=}')


# 合法
fun(1, 2, 3, 4, e=5, f=6)
# 合法
fun(1, 2, 3, d=4, e=5, f=6)
# 合法
fun(1, 2, c=3, d=4, e=5, f=6)
# 不合法
fun(1, b=2, c=3, d=4, e=5, f=6)
# 不合法
fun(a=1, b=2, c=3, d=4, e=5, f=6)