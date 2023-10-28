import json
import copy

p2c_dict = {}


# 生成拼音汉字对照表
def p2c_dict_gen():
    # 读入文件
    p2c_file = open("../data/拼音汉字表/拼音汉字表.txt", encoding="gbk")
    c_file = open("../data/拼音汉字表/一二级汉字表.txt", encoding="gbk")
    p2c_lines = p2c_file.readlines()
    c_str = c_file.readline().strip()
    p2c_file.close()
    c_file.close()

    # 生成p2c字典
    for p2c_line in p2c_lines:
        p2c_line = p2c_line.strip().split()
        p2c_list = []
        for c in p2c_line[1:]:
            # 检验是否为一二级
            if c in c_str:
                p2c_list.append(c)
        p2c_dict[p2c_line[0]] = p2c_list


# 将拼音汉字对照表存储到参数设置的地址
def save(p2c_path):
    save_file = open(p2c_path, "w")
    json.dump(p2c_dict, save_file)
    save_file.close()


# 根据参数中给出的单字表修改拼音汉字对照表并保存
def modify(p2c_path, single_path):
    p2c_json = open(p2c_path)
    p2c_dict = json.load(p2c_json)
    p2c_json.close()
    single_json = open(single_path)
    single_dict = json.load(single_json)
    single_json.close()

    # 将单字表中没有的字删去
    for values in list(p2c_dict.values()):
        values_copy = copy.deepcopy(values)
        for value in values_copy:
            if value not in list(single_dict.keys()):
                values.remove(value)

    save(p2c_path)
