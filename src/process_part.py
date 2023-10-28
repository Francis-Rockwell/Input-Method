import math
import settings


# 处理首字符
def process_first(pinyin: str):
    settings.cost = {}

    c_candidates = settings.P2C_DICT[pinyin]
    for c_candidate in c_candidates:
        # p1为该字符在首字符表中出现的频率
        p1 = float(settings.FIRST_DICT.get(c_candidate, 0)) / settings.FIRST
        # p2为该字符在单字符表中出现的频率，用于平滑处理
        p2 = float(settings.SINGLE_DICT[c_candidate]) / settings.SINGLE
        # 平滑处理
        p = settings.ARGS.LAMBDA*p1 + (1 - settings.ARGS.LAMBDA) * p2
        # 取对数在取负，转为加法取最小值，使用viterbi算法，cost中记载各个首字符的代价
        settings.cost[c_candidate] = -math.log(p)


# 二元字模型处理函数
def process_two(pinyin: str):

    tmp = {}
    c_candidates = settings.P2C_DICT[pinyin]
    for c_candidate in c_candidates:
        min = float("inf")
        key = ""
        for prefix in list(settings.cost.keys()):
            # 在目前的cost表中选取使得自己代价最小的前缀，并更新代价表
            # p1为已知前一个字符prefix[-1]的条件下，下一个字符是该字符的条件概率，
            # 用二元字模型中他们组合出现的频次 除以 prefix[-1]本身出现的频次得到
            p1 = float(settings.FREQ2_DICT.get(prefix[-1] + c_candidate, 0)) / settings.SINGLE_DICT[prefix[-1]]
            # p2为该字符在单字符表中出现的的频率，用于平滑处理
            p2 = float(settings.SINGLE_DICT[c_candidate]) / settings.SINGLE
            # 取对数取反，加上前缀的总代价，得到由该路径到该字符的代价
            p = -math.log(settings.ARGS.LAMBDA*p1 + (1-settings.ARGS.LAMBDA) * p2) + settings.cost[prefix]
            # 在所有前缀到该字符的代价中取最小
            if p < min:
                key = prefix + c_candidate
                min = p
        tmp[key] = min
    # 更新代价表
    settings.cost = tmp


# 三元字模型处理函数
def process_three(pinyin: str):

    tmp = {}
    c_candidates = settings.P2C_DICT[pinyin]
    for c_candidate in c_candidates:
        min = float("inf")
        key = ""
        for prefix in list(settings.cost.keys()):
            # p1为已知前两个字符prefix[-2:]的条件下，下一个字符是该字符的条件概率，
            # 用三元字模型中他们组合出现的频次 除以 prefix[-2:]本身出现的频次得到
            # 若prefix[-2:]在二元字模型中未曾出现过，条件概率取0
            p1 = float(settings.FREQ3_DICT.get(prefix[-2:] + c_candidate, 0)) / settings.FREQ2_DICT[prefix[-2:]] \
                    if prefix[-2:] in settings.FREQ2_DICT.keys() \
                    else 0
            # 后续处理过程同二元字模型
            p2 = float(settings.SINGLE_DICT[c_candidate]) / settings.SINGLE
            p = -math.log(settings.ARGS.LAMBDA*p1 + (1 - settings.ARGS.LAMBDA) * p2) + settings.cost[prefix]
            if p < min:
                key = prefix + c_candidate
                min = p
        tmp[key] = min
    settings.cost = tmp
