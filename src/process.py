import settings
from process_part import process_first, process_two, process_three


# process函数完成对输入拼音的处理
def process():

    settings.outputs = []

    print("正在处理拼音")

    for input_line in settings.INPUT_LINES:
        inputs = input_line.split()

        # 处理首字符
        process_first(inputs[0])

        # 若为二元字模型
        if settings.ARGS.TYPE % 2:
            for pinyin in inputs[1:]:
                process_two(pinyin)
        # 若为三元字模型
        else:
            # 第二个字符仍采用二元字模型
            process_two(inputs[1])
            # 第三个字符开始采用三元字模型
            for pinyin in inputs[2:]:
                process_three(pinyin)

        # 为了排序，先用代价表生成(key, value)的列表
        sen_cost_list = []
        for candidate in list(settings.cost.keys()):
            sen_cost_list.append((candidate, settings.cost[candidate]))

        # 根据value，也就是cost的大小进行排序
        def takeSecond(elem):
            return elem[1]
        sen_cost_list.sort(key=takeSecond)

        # 对每条拼音输出代价最小的TOP个处理结果（可能的结果不足TOP个则全部输出）
        candidates = []
        RANGE = settings.ARGS.TOP if len(sen_cost_list) >= settings.ARGS.TOP else len(sen_cost_list)
        for sen_cost in sen_cost_list[:RANGE]:
            candidates.append(sen_cost[0])

        settings.outputs.append(candidates)
