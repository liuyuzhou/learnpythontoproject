def use_finally(x, y):
    try:
        a = x/y
    finally:
        print('No matter what happened,I will show in front of you')


use_finally(2, 0)
