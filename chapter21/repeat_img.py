# 图片重复检测
import os
import time
import shutil
import hashlib

from PIL import Image

# FILE_SUFFIX_PATH = 'D:/public lession/files/image'
FILE_SUFFIX_PATH = 'images'


def image_read_and_repeat_check():
    """
    图片读取并做重复检测
    :return:
    """
    # 取得指定目录下所有文件
    image_list = os.listdir(FILE_SUFFIX_PATH)
    image_read_key_id_dict = dict()
    id_image_full_path_dict = dict()
    # 遍历文件
    for img_name in image_list:
        try:
            # 图片全路径
            full_image_path_name = os.path.join(FILE_SUFFIX_PATH, img_name)
            # 图片路径中的 字符替换
            full_image_path_name = full_image_path_name.replace("\\", "/")
            if full_image_path_name is None or full_image_path_name.find('_') < 0:
                continue

            # 字符串截取并取得最后一位
            key_id_str = full_image_path_name.split('_')[-1]
            # 字符串截取取得倒数第二个
            key_id = int(key_id_str.split('.')[-2])
            # 字典数据添加
            id_image_full_path_dict[key_id] = full_image_path_name
            tt = time.time()
            # 文件是否破损检查
            Image.open(full_image_path_name).verify()
            # Image.open(full_image_path_name).load()
            with open(full_image_path_name, 'rb') as f:
                # 用hash加密
                sha1obj = hashlib.sha1()
                sha1obj.update(f.read())
                # 取得加密结果
                i_img_str = sha1obj.hexdigest()
            # 字典中是否存在hash加密结果
            key_id_list = image_read_key_id_dict.get(i_img_str)
            print(i_img_str)
            if key_id_list is None or len(key_id_list) == 0:
                # 不存在hash加密结果，将hash加密结果与对应id集合以键值对存入字典
                no_key_id_list = list()
                no_key_id_list.append(key_id)
                image_read_key_id_dict[i_img_str] = no_key_id_list
                continue
            # 存在相同hash结果，将id加入id集合
            key_id_list.append(key_id)
            image_read_key_id_dict[i_img_str] = key_id_list
        except Exception as ex:
            print(f'read error:{ex}')
            continue

    # 找到并更新重复图片
    find_and_update_repeat_image(image_read_key_id_dict, id_image_full_path_dict)


def find_and_update_repeat_image(image_read_key_id_dict, id_image_full_path_dict):
    """
    找到并更新重复图片
    :param image_read_key_id_dict:
    :param id_image_full_path_dict:
    :return:
    """
    if image_read_key_id_dict is None or len(image_read_key_id_dict) <= 1:
        return

    update_id_list = list()
    id_images_dict = dict()
    cycle_num = 0
    # 遍历字典
    for repeat_id_list in image_read_key_id_dict.values():
        # 遍历键值对中的值，值为None或值长度小于1，则表示没有重复图片
        if repeat_id_list is None or len(repeat_id_list) <= 1:
            continue

        min_id = min(repeat_id_list)
        print(f'该批次的所有相似图片：{repeat_id_list}')
        # print('保留id最小图片：', min_id)
        id_images_dict[min_id] = set(repeat_id_list)
        # repeat_id_list.remove(min_id)
        # 将重复图片分别保存到不同文件夹
        repeat_file_store(str(cycle_num), repeat_id_list, id_image_full_path_dict)
        cycle_num += 1


def repeat_file_store(cycle_num, repeat_id_list, id_image_full_path_dict):
    """
    重复图片存储
    :param cycle_num:
    :param repeat_id_list:
    :param id_image_full_path_dict:
    :return:
    """
    # 重复文件全路径
    # repeat_file_path = os.path.join('D:/public lession/files/repeat/', cycle_num)
    repeat_file_path = os.path.join('repeat', cycle_num)
    try:
        # 如果对应文件不存在，则创建
        if os.path.exists(repeat_file_path) is False:
            os.makedirs(repeat_file_path)
    except Exception as ex:
        print(f'error:{ex}')
    # 遍历id集合
    for key_id in repeat_id_list:
        # 取得对应图片
        image = id_image_full_path_dict.get(key_id)
        image_name = image.split('/')[-1]
        # 目标图片全路径
        repeat_file_full_path = repeat_file_path + '/' + image_name
        # 从原路径拷贝至目标路径
        shutil.copyfile(image, repeat_file_full_path)


if __name__ == "__main__":
    start_time = time.time()
    image_read_and_repeat_check()
    spend_time = time.time() - start_time
    print(f'total spend:{spend_time}s')
