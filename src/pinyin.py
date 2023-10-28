import time
from args import parse
from load import load
from process import process
from save import save
from check import check


if __name__ == "__main__":
    # parse函数完成对命令行参数的解析
    parse()
    # load函数完成从各个文件中的加载
    load()
    # process函数完成对输入拼音的处理
    start = time.time()
    process()
    end = time.time()
    print("处理耗时：%fs" % (end-start))
    # save函数完成对处理结果的写入保存
    save()
    # check函数完成对处理结果的评测
    check()
