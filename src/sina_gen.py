import os
import json
import re
import p2c_gen

path = "../data/语料库/sina_news_gbk/"
sina_files_names = os.listdir(path=path)[:-1]
freq2_dict = {}
first_dict = {}
single_dict = {}
c_str = open("../data/拼音汉字表/一二级汉字表.txt", encoding="gbk").readline().strip()
p2c_path = "./sina_p2c_dict.json"
freq2_path = "./sina_freq2_dict.json"
single_path = "./sina_single_dict.json"
first_path = "./sina_first_dict.json"


# 生成sina_fre2_dict.json、sina_single_dict.json、sina_first_dict.json
def sina_gen():
    for sina_file_name in sina_files_names:
        sina_file = open(path+sina_file_name, encoding="gbk")
        sina_lines = sina_file.readlines()
        for sina_line in sina_lines:
            sina_json = json.loads(sina_line)
            sina_html = sina_json['html']
            sina_title = sina_json['title']

            # 在html字段统计连着的两个字
            for index in range(len(sina_html)-1):
                if sina_html[index] in c_str \
                        and sina_html[index+1] in c_str:
                    freq2_dict[sina_html[index:index+2]] \
                            = freq2_dict.get(sina_html[index:index+2], 0) + 1

            # 用标点分割得到字句，统计首字符
            sentences = re.split('。| |，|！|？|：|；', sina_html)
            for sentence in sentences:
                for c in sentence:
                    if c in c_str:
                        first_dict[c] = first_dict.get(c, 0) + 1
                        break

            # 统计单个字符
            for c in sina_html:
                if c in c_str:
                    single_dict[c] = single_dict.get(c, 0) + 1

            # 下同，在title字段中统计
            for index in range(len(sina_title) - 1):
                if sina_title[index] in c_str \
                        and sina_title[index+1] in c_str:
                    freq2_dict[sina_title[index:index+2]] \
                            = freq2_dict.get(sina_title[index:index+2], 0) + 1

            sentences = re.split('。| |，|！|？|：|；', sina_title)
            for sentence in sentences:
                for c in sentence:
                    if c in c_str:
                        first_dict[c] = first_dict.get(c, 0) + 1
                        break

            for c in sina_html:
                if c in c_str:
                    single_dict[c] = single_dict.get(c, 0) + 1

        sina_file.close()

    save_file = open(freq2_path, "w")
    json.dump(freq2_dict, save_file)
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
    sina_gen()
    p2c_gen.modify(p2c_path, single_path)
