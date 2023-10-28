import os
import json

path = "../data/语料库/sina_news_gbk/"
sina_files_names = os.listdir(path=path)[:-1]
freq3_dict = {}
first_dict = {}
single_dict = {}
c_str = open("../data/拼音汉字表/一二级汉字表.txt", encoding="gbk").readline().strip()
freq3_path = "./sina_freq3_dict.json"


# 生成sina_freq3_dict.json
def sina_gen3():
    for sina_file_name in sina_files_names:
        sina_file = open(path+sina_file_name, encoding="gbk")
        sina_lines = sina_file.readlines()
        for sina_line in sina_lines:
            sina_json = json.loads(sina_line)
            sina_html = sina_json['html']
            sina_title = sina_json['title']

            # 统计连续的3个字符，方法与sina_gen.py中中相同
            for index in range(len(sina_html)-1):
                if sina_html[index] in c_str \
                        and sina_html[index+1] in c_str:
                    freq3_dict[sina_html[index:index+2]] \
                            = freq3_dict.get(sina_html[index:index+2], 0) + 1

            # 在title字段统计
            for index in range(len(sina_title) - 1):
                if sina_title[index] in c_str \
                        and sina_title[index+1] in c_str:
                    freq3_dict[sina_title[index:index+2]] \
                            = freq3_dict.get(sina_title[index:index+2], 0) + 1

        sina_file.close()

    save_file = open("SMP_freq3_dict.json", "w")
    json.dump(freq3_dict, save_file)
    save_file.close()


if __name__ == "__main__":
    sina_gen3()
