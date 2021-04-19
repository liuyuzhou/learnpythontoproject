def model_exception(x, y):
    try:
        b = name
        a = x/y
    except (ZeroDivisionError, NameError, TypeError) as e:
        print(e)


model_exception(2, 0)
