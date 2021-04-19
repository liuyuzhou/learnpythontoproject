import datetime

dt = datetime.datetime.now()
old_dt = str(dt)
new_dt = dt.strptime(old_dt, '%Y-%m-%d %H:%M:%S.%f')
print(f"old_dt is:{old_dt}")
print(f"old_dt type is:{type(old_dt)}")
print(f"new_dt is:{new_dt}")
print(f"new_dt type is:{type(new_dt)}")
