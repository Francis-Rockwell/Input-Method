import json
import settings


# load函数完成对各个文件的加载
def load():

    print("正在加载词频表")

    # 加载拼音-字符映射表
    p2c_json = open(settings.ARGS.p2c_path)
    settings.P2C_DICT = json.load(p2c_json)
    p2c_json.close()

    # 加载二元字模型词频表
    freq2_json = open(settings.ARGS.freq2_path)
    settings.FREQ2_DICT = json.load(freq2_json)
    freq2_json.close()

    # 新浪的三元字模型词频表较大，加载时间较长，提示等待
    if settings.ARGS.TYPE == 2:
        print("词频表较大，请耐心等待")

    # 第2、4种情况加载三元字模型表
    if settings.ARGS.TYPE % 2 == 0:
        freq3_json = open(settings.ARGS.freq3_path)
        settings.FREQ3_DICT = json.load(freq3_json)
        freq3_json.close()

    # 加载首字符频率表
    first_json = open(settings.ARGS.first_path)
    settings.FIRST_DICT = json.load(first_json)
    first_json.close()

    # 加载单字符频率表
    single_json = open(settings.ARGS.single_path)
    settings.SINGLE_DICT = json.load(single_json)
    single_json.close()

    # 读取拼音输入文件
    input_file = open(settings.ARGS.input_path)
    settings.INPUT_LINES = input_file.readlines()
    input_file.close()

    # 绑定输出文件、标准输出文件
    settings.OUTPUT_FILE = open(settings.ARGS.output_path, "w")
    settings.STD_FILE = open(settings.ARGS.std_path, encoding="utf-8")

    # 计数首字符频率表和单字符频率表中的总频次数，方便后续处理成频率
    settings.FIRST = sum(list(settings.FIRST_DICT.values()))
    settings.SINGLE = sum(list(settings.SINGLE_DICT.values()))

    # 把二元字模型词频表中出现次数低于LOWERBOUND的词删去
    for key in list(settings.FREQ2_DICT.keys()):
        if settings.FREQ2_DICT[key] < settings.ARGS.LOWERBOUND:
            del settings.FREQ2_DICT[key]

    # 把三元字模型词频表中出现频次低于LOWERBOUND的词删去
    if settings.ARGS.TYPE % 2 == 0:
        for key in list(settings.FREQ3_DICT.keys()):
            if settings.FREQ3_DICT[key] < settings.ARGS.LOWERBOUND:
                del settings.FREQ3_DICT[key]
