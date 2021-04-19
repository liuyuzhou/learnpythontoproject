import os
import time


from PIL import Image

# IMAGE_PATH = 'D:/public lession/files/broken_img'
IMAGE_PATH = 'images'


def image_is_broken_check():
    """
    检测破损图片
    :return:
    """
    start_time = time.time()
    # 取得指定目录下所有图片
    img_name_list = os.listdir(IMAGE_PATH)
    # 遍历取得图片
    for img_name in img_name_list:
        # 图片全路径
        local_img_path = os.path.join(IMAGE_PATH, img_name)
        # print('image name:{}'.format(img_name))
        # print(f'image name:{img_name}')
        try:
            # 打开并确认给定的图像文件，这个是一个懒操作；该函数只会
            # 读文件头，而真实的图像数据直到试图处理该数据才会从文件
            # 读取（调用load()方法将强行加载图像数据），加载失败，抛
            # 异常
            Image.open(local_img_path).verify()
            Image.open(local_img_path).load()
            print(f'图片正常:{img_name}')
        except Exception as ex:
            print(f'图片 ({img_name}) 破损，不能正确读取，异常原因:{ex}')
            continue
    print(f'total spend:{1000 * (time.time() - start_time)} ms')


if __name__ == "__main__":
    image_is_broken_check()
