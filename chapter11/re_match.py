import re

# 在起始位置匹配
print(re.match('hello', 'hello world').span())
# 不在起始位置匹配
print(re.match('world', 'hello world'))
