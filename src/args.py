import argparse
import settings


# 定义了完整的全局参数的类型
class COMPLETE_ARGS:
    def __init__(self, TYPE=1, LAMBDA=0.999999, LOWERBOUND=1, TOP=1, ACCURACY=1.0,
                 INPUT="../data/input.txt", OUTPUT="../data/output.txt"):
        self.TYPE = TYPE
        self.LAMBDA = LAMBDA
        self.LOWERBOUND = LOWERBOUND
        self.TOP = TOP
        self.ACCURACY = ACCURACY
        self.input_path = INPUT
        self.output_path = OUTPUT
        self.std_path = "../data/std_output.txt"

        # 从新浪数据中加载
        if TYPE <= 2:
            self.p2c_path = "./sina_p2c_dict.json"
            self.freq2_path = "./sina_freq2_dict.json"
            self.freq3_path = "./sina_freq3_dict.json"
            self.first_path = "./sina_first_dict.json"
            self.single_path = "./sina_single_dict.json"
        # 从微博数据中加载
        else:
            self.p2c_path = "./SMP_p2c_dict.json"
            self.freq2_path = "./SMP_freq2_dict.json"
            self.freq3_path = "./SMP_freq3_dict.json"
            self.first_path = "./SMP_first_dict.json"
            self.single_path = "./SMP_single_dict.json"


# parse函数完成对命令行参数的处理
def parse():

    print("正在解析参数")

    # 定义命令行参数，各个参数的定义见help
    parser = argparse.ArgumentParser()
    parser.add_argument("--TYPE", "-t", help="TYPE参数用于设置输入法模式，默认为1 \
                                            模式1为新浪新闻语料库，二元字模型; \
                                            模式2为新浪新闻语料库，三元字模型; \
                                            模式3为微博语料库，二元字模型; \
                                            模式4为微博语料库，三元字模型;",
                        metavar="TYPE", type=int, default=1)
    parser.add_argument("--LAMBDA", "-L", help="LAMBDA参数用于平滑处理，默认为0.999999",
                        metavar="LAMBDA", type=float, default=0.999999)
    parser.add_argument("--LOWERBOUND", "-l", help="LOWERBOUND参数用于设置词频表中词频下限，默认为1",
                        metavar="LOWERBOUND", type=int, default=1)
    parser.add_argument("--TOP", "-T", help="TOP参数用于设置每句拼音输出的句子个数，默认为1",
                        metavar="TOP", type=int, default=1)
    parser.add_argument("--ACCURACY", "-A", help="ACCURACY参数用于设置认为一句拼音处理结果正确的最低的单句字准确比例，默认为1.0",
                        metavar="ACCURACY", type=float, default=1.0)
    parser.add_argument("PATH", default=["../data/input.txt", "../data/output.txt"], nargs="*")

    # 解析命令行参数并将其处理为完整版的参数类型COMPLETE_ARGS
    argument = parser.parse_args()
    settings.ARGS = COMPLETE_ARGS(int(argument.TYPE), float(argument.LAMBDA), int(argument.LOWERBOUND),
                                  int(argument.TOP), float(argument.ACCURACY), argument.PATH[0], argument.PATH[1])
