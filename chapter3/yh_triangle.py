# 生成杨辉三角的一行
def create_line(l_list):
    line_list = [1]
    for x in range(1, len(l_list)):
        line_list.append(l_list[x] + l_list[x - 1])
    line_list.append(1)
    return line_list


# 打印
def print_line(line_list, width_v):
    s = ""
    for x in line_list:
        s += str(x) + "  "
    print(s.center(width_v))


lines = [1]
row = int(input("输入行数："))
# 设置打印宽度
width = row * 4
for x in range(row):
    print_line(lines, width)
    lines = create_line(lines)
