import time

t = (2020, 10, 25, 12, 15, 38, 6, 48, 0)
t = time.mktime(t)
print(time.strftime('%b %d %Y %H:%M:%S', time.gmtime(t)))
