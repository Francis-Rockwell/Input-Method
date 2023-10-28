import settings


# check函数完成对处理结果的评测，打印句正确率和字正确率
def check():

    print("正在自动测评")

    # 读取文件
    settings.OUTPUT_FILE = open(settings.ARGS.output_path)
    stds_pre = settings.STD_FILE.readlines()
    outs_pre = settings.OUTPUT_FILE.readlines()
    settings.STD_FILE.close()
    settings.OUTPUT_FILE.close()

    # 初始化变量，大写表示总数，小写表示正确的数目
    stds = []
    outs = []
    SENTENCES = len(stds_pre)
    sentences = 0
    CHARACTERS = 0
    characters = 0
    mean = 0

    # stds和outs分别存储读入结果strip后的结果
    for std in stds_pre:
        stds.append(std.strip())
    for out in outs_pre:
        outs.append(out.strip().split())

    # 循环检查句子和字符的正确率
    for i in range(SENTENCES):
        # 计数总字符数
        CHARACTERS += len(stds[i])
        # max表示单句处理的所有候选结果中字符正确最多的值
        max = 0
        for j in range(len(outs[i])):
            count = 0
            # 计数该候选结果中的正确字符数
            for k in range(len(stds[i])):
                if outs[i][j][k] == stds[i][k]:
                    count += 1
            if count > max:
                max = count
            # 该候选结果与标准答案完全一致，增加句准确数
        mean += (float(max) / len(stds[i])) / SENTENCES
        if float(max) >= settings.ARGS.ACCURACY * len(stds[i]):
            sentences += 1
        characters += max

    print("句准确率：%f%%" % (float(sentences) / SENTENCES * 100))
    print("字准确率：%f%%" % (float(characters) / CHARACTERS * 100))
    print("平均单句字准确比例：%f%%" % (mean * 100))
