import re

line = 'Cats are smarter than dogs'

if matchObj := re.match(r'dogs', line, re.M | re.I):
    print(f'use match,the match string is: {matchObj.group()}')
else:
    print("No match string!!")

if matchObj := re.search( r'dogs', line, re.M | re.I):
    print(f'use search,the match string is: {matchObj.group()}')
else:
    print("No match string!!")
