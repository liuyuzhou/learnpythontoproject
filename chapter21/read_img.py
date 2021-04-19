import os

from PIL import Image

# IMG_PATH = 'D:/python lession/files/image'
IMG_PATH = 'images'


def img_read():
    """
    图片尺寸读取
    :return:
    """
    # 取得指定路径下所有文件
    img_name_list = os.listdir(IMG_PATH)
    # 文件遍历
    for name in img_name_list:
        try:
            local_img_path = os.path.join(IMG_PATH, name)
            # 图像数据加载
            Image.open(local_img_path).load()
            # 打开并确认给定的图像文件
            img = Image.open(local_img_path)
            # 图像尺寸
            img_size = img.size
            # 图像高度
            img_height = img_size[0]
            # 图像宽度
            img_width = img_size[1]
            # 色彩模式
            img_color = img.mode
            print(f'图片名：{name}，图片高：{img_height}，'
                  f'图片宽：{img_width}，图片色彩模式：{img_color}')
            # break
        except Exception as ex:
            print(f'图片尺寸读取失败:{name}')


if __name__ == "__main__":
    img_read()
