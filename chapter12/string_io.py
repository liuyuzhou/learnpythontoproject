from io import StringIO

io_val = StringIO()
io_val.write('hello')
print(f'say:{io_val.getvalue()}')
