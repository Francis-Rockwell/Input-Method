import json
import re
import p2c_gen

path = "../data/语料库/SMP2020/usual_train_new.txt/"
freq2_dict = {}
freq3_dict = {}
first_dict = {}
single_dict = {}
c_str = open("../data/拼音汉字表/一二级汉字表.txt", encoding="gbk").readline().strip()
p2c_path = "./SMP_p2c_dict.json"
freq2_path = "./SMP_freq2_dict.json"
freq3_path = "./SMP_freq3_dict.json"
single_path = "./SMP_single_dict.json"
first_path = "./SMP_first_dict.json"


# 生成SMP_p2c_dict.json、SMP_freq2_dict.json、SMP_freq3_dict.json、SMP_single_dict.json、SMP_first_dict.json
def SMP_gen():
    SMP_file = open(path, encoding="gbk")
    SMP_lines = SMP_file.readlines()
    for SMP_line in SMP_lines:
        # 数据集比较丑陋，需要预处理成可以json化的格式
        SMP_line = SMP_line.replace(' "', " '")
        SMP_line = SMP_line.replace('",', "',")
        SMP_line = SMP_line.replace('"', '')
        SMP_line = SMP_line.replace("'id'", '"id"')
        SMP_line = SMP_line.replace("'content'", '"content"')
        SMP_line = SMP_line.replace("'label'", '"label"')
        SMP_line = SMP_line.replace(" '", ' "')
        SMP_line = SMP_line.replace("',", '",')
        SMP_line = SMP_line.replace("'}", '"}')
        SMP_line = SMP_line.replace("\\xa0", '')
        SMP_json = json.loads(SMP_line)
        SMP_content = SMP_json['content']

        # 连续2个字
        for index in range(len(SMP_content)-1):
            if SMP_content[index] in c_str \
                    and SMP_content[index+1] in c_str:
                freq2_dict[SMP_content[index:index+2]] \
                        = freq2_dict.get(SMP_content[index:index+2], 0) + 1

        # 连续3个字
        for index in range(len(SMP_content)-2):
            if SMP_content[index] in c_str \
                    and SMP_content[index+1] in c_str \
                    and SMP_content[index+2] in c_str:
                freq3_dict[SMP_content[index:index+3]] \
                        = freq3_dict.get(SMP_content[index:index+3], 0) + 1

        # 首字
        sentences = re.split('。| |，|！|？|：|；', SMP_content)
        for sentence in sentences:
            for c in sentence:
                if c in c_str:
                    first_dict[c] = first_dict.get(c, 0) + 1
                    break

        # 单字
        for c in SMP_content:
            if c in c_str:
                single_dict[c] = single_dict.get(c, 0) + 1

    SMP_file.close()

    save_file = open(freq2_path, "w")
    json.dump(freq2_dict, save_file)
    save_file.close()
    save_file = open(freq3_path, "w")
    json.dump(freq3_dict, save_file)
    save_file.close()
    save_file = open(first_path, "w")
    json.dump(first_dict, save_file)
    save_file.close()
    save_file = open(single_path, "w")
    json.dump(single_dict, save_file)
    save_file.close()


if __name__ == "__main__":
    p2c_gen.p2c_dict_gen()
    p2c_gen.save(p2c_path)
    SMP_gen()
    p2c_gen.modify(p2c_path, single_path)
