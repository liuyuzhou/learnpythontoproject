import os

# PATH_PRE = 'D:/python lession/files/image'
PATH_PRE = 'images'


def rename_image():
    """
    图片重命名
    :return:
    """
    # 取得指定路径下所有文件
    image_name_list = os.listdir(PATH_PRE)
    num_i = 1
    # 遍历文件
    for name in image_name_list:
        # 原始全路径
        primary_full_path = os.path.join(PATH_PRE, name)
        # 文件新名称
        new_name = f'elt_{str(num_i)}.jpg'
        # 文件更名后的全路径名
        img_full_path = os.path.join(PATH_PRE, new_name)
        print(f'图片原名称：{name}，新名称：{new_name}')
        # 重命名
        os.rename(primary_full_path, img_full_path)
        num_i += 1


if __name__ == "__main__":
    rename_image()
