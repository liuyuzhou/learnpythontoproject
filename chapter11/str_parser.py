# coding=UTF-8
import re

str_num_pat = re.compile(r'[一二三四五六七八九十]')
str_pat = re.compile(r'[一二三四五六七八九十]\s{0,3}[万千wk]')
str_num_dict = {'一': '1', '二': '2', '三': '3', '四': '4', '五': '5',
                '六': '6', '七': '7', '八': '8', '九': '9', '十': '10'}
conn_pat = re.compile(r'[~\-–—―－一至]')


def ch_num_to_number(str_val):
    """
    将 str_val 中类似 一万 的字符 更改为 1万
    :param str_val:
    :return:
    """
    if not str_num_pat.search(str_val) or not str_pat.search(str_val):
        return str_val

    str_num_list = str_num_pat.findall(str_val)
    str_sal_list = str_pat.findall(str_val)

    # 满足如下 if 条件时，根据 str_num_list 中值修改 str_val 对应字符值
    if (len(str_num_list) <= len(str_sal_list)) \
            or (len(str_num_list) == len(str_sal_list) + 1
                and conn_pat.search(str_val)):
        for str_num in str_num_list:
            num_val = str_num_dict.get(str_num)
            str_val = str_val.replace(str_num, num_val)
    else:
        # 根据 str_sal_list 中值修改 str_val 对应字符值
        for str_num in str_sal_list:
            b_sal_val = str_val[0: str_val.find(str_num)]
            e_sal_val = str_val[str_val.find(str_num) + len(str_num):]
            find_str = str_val[str_val.find(str_num): str_val.find(str_num) + len(str_num)]
            num_s = str_num_pat.search(str_num).group()
            num_val = str_num_dict.get(num_s)
            find_str = find_str.replace(num_s, num_val)
            str_val = b_sal_val + find_str + e_sal_val

    return str_val


if __name__ == "__main__":
    pri_str = '二万'
    fmt_result = ch_num_to_number('二万')
    print(f'原字符串： {pri_str}。格式化后的结果：{fmt_result}')
    pri_str = '二万-三万'
    fmt_result = ch_num_to_number('二万-三万')
    print(f'原字符串： {pri_str}。格式化后的结果：{fmt_result}')
