import datetime

dt = datetime.datetime.now()
new_dt = dt.strftime('%Y-%m-%d %H:%M:%S')
print(f"dt is: {dt}")
print(f"dt type is:{type(dt)}")
print(f"new_dt is:{new_dt}")
print(f"new_dt type is:{type(new_dt)}")
