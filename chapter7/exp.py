def exp(p1, p2, df=0, *vart, **kw):
    print(f'{p1 = }, {p2 = }, {df = }, {vart = }, {kw = }')


exp(1, 2)
exp(1, 2, c=3)
exp(1, 2, 3, 'a', 'b')
exp(1, 2, 3, 'abc', x=9)
