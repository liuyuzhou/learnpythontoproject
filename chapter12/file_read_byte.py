path = './test.txt'
f_name = open(path, 'w')
print(f"write length:{f_name.write('Hello')}")
f_name = open(path)
while c_str := f_name.read(1):
    print(f'read str is:{c_str}')
    c_str = f_name.read(1)
f_name.close()
