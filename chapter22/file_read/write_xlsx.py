# coding=UTF-8
import xlrd
import openpyxl


def write_xlsx_file(sheet_obj, sheet_name):
    """
    xlsx 文件写入
    :param sheet_obj:
    :param sheet_name:
    :return:
    """
    row_list = list()
    # 按行遍历读取xlsx文件内容
    for i in range(sheet_obj.nrows):
        row = sheet_obj.row_values(i)
        row_list.append(row)

    # 实例化 Workbook 对象
    workbook = openpyxl.Workbook()
    # 获取当前活跃的worksheet对象
    new_sheet = workbook.active
    # sheet 页命名
    new_sheet.title = 'xlsx_write'

    # 循环便利 list 集合对象
    for i in range(len(row_list)):
        for j in range(0, len(row_list[i])):
            # 将读取数据插入 sheet 页指定行和列
            new_sheet.cell(row=i + 1, column=j + 1, value=str(row_list[i][j]))
    # 保存工作薄，命名为 xlsx_write.xlsx
    workbook.save(f'./files/{sheet_name}')
    print('xlsx格式表格写入数据成功！')


if __name__ == "__main__":
    # 打开 excel 文件读取数据
    book = xlrd.open_workbook('./files/basic_info.xlsx')
    # 通过名称获取 book 中的一个工作表
    sheet = book.sheet_by_name('basic_info')
    sheet_name = 'xlsx_write.xlsx'
    write_xlsx_file(sheet, sheet_name)
