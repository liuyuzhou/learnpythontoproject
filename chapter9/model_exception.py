def model_exception(x, y):
    try:
        b = name
        a = x/y
    except (ZeroDivisionError, NameError, TypeError):
        print('one of ZeroDivisionError or NameError or TypeError happened')


model_exception(2,0)
