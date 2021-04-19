def pow(x, y, z=None):
    r = x ** y
    if z is not None:
       r %= z
       return r


print(f'{pow(2, 10, 5)=}')
print(f'{pow(2, 10, z=5)=}')
