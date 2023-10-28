# README

## 项目介绍

​		Replanted course porject from my Introduction to AI class

​		本项目为使用马尔科夫方法以及viterbi算法实现的简易拼音输入法。

## 文件结构

.
├── README.md
├── data
│   ├── input.txt
│   ├── output.txt
│   └── std_output.txt
└── src
    ├── SMP_gen_2&3.py
    ├── args.py
    ├── check.py
    ├── load.py
    ├── p2c_gen.py
    ├── pinyin.py
    ├── process.py
    ├── process_part.py
    ├── save.py
    ├── settings.py
    ├── sina_first_dict.json
    ├── sina_freq2_dict.json
    ├── sina_gen.py
    ├── sina_gen3.py
    ├── sina_p2c_dict.json
    └── sina_single_dict.json

## 使用方法

​		环境要求：python3

​		运行方法：进入src文件夹，使用“python pinyin.py”运行程序

​		命令行参数：

​		参数一：“python pinyin.py input_path output_path”依次指定输入输出文件地址，默认输入文件地址为“../data/input.txt”，默认文件输出地址为“../data/output.txt”。输入与标准输出文件的编码模式为utf-8，输出文件的编码模式为gbk。

​		参数二：“python pinyin.py -t ”，或“python pinyin.py --TYPE ”，TYPE参数用于设置输入法模式，默认为1，模式1为新浪新闻语料库，二元字模型;；模式2为新浪新闻语料库，三元字模型；模式3为微博语料库，二元字模型；模式4为微博语料库，三元字模型。

​		参数三：“python pinyin.py -L ”，或“python pinyin.py --LAMBDA ”，LAMBDA参数用于平滑处理，默认为0.999999。

​		参数四：“python pinyin.py -l ”，或“python pinyin.py --LOWERBOUND ”，LOWERBOUND参数用于设置词频表中词频下限，默认为1。

​		参数五：“python pinyin.py -T ”，或“python pinyin.py --TOP ”，"TOP参数用于设置每句拼音输出的句子个数，默认为1。

​		参数六：“python pinyin.py -A ”，或“python pinyin.py --ACCURACY ”，ACCURACY参数用于设置认为一句拼音处理结果正确的最低的单句字准确比例，默认为1.0

​		注：以上参数均可互相搭配使用。

​		如果只体验基础要求，不需要下载额外的文件，但注意**不要在程序运行时使用-t参数**。

​		如果要体验附加功能方法一是**从https://cloud.tsinghua.edu.cn/d/70fbb2ae255f44308ecb/下载sina_freq3_dict.json、SMP_first_dict.json、SMP_freq2_dict.json、SMP_p2c_dict.json、SMP_single_dict.json共6个文件，将其拷贝到./src中，形成如下结构**，

.
├── README.md
├── data
│   ├── input.txt
│   ├── output.txt
│   └── std_output.txt
└── src
    ├── **SMP_first_dict.json**
    ├── **SMP_freq2_dict.json**
    ├── **SMP_freq3_dict.json**
    ├── SMP_gen_2&3.py
    ├── **SMP_p2c_dict.json**
    ├── **SMP_single_dict.json**
    ├── args.py
    ├── check.py
    ├── load.py
    ├── p2c_gen.py
    ├── pinyin.py
    ├── process.py
    ├── process_part.py
    ├── save.py
    ├── settings.py
    ├── sina_first_dict.json
    ├── sina_freq2_dict.json
    ├── **sina_freq3_dict.json**
    ├── sina_gen.py
    ├── sina_gen3.py
    ├── sina_p2c_dict.json
    └── sina_single_dict.json

后续运行方法和参数同上，且可以通过-t参数选择运行模式

​		方法二是**从https://cloud.tsinghua.edu.cn/d/8712d759def745cb8bae/下载语料库.zip和拼音汉字表.zip，解压后放在src文件夹内，形成如下结构：**

.
├── README.md
├── data
│   ├── input.txt
│   ├── output.txt
│   ├── std_output.txt
│   ├── **拼音汉字表**
│   │   ├── README.txt
│   │   ├── 一二级汉字表.txt
│   │   └── 拼音汉字表.txt
│   └── **语料库**
│       ├── SMP2020
│       │   ├── README.txt
│       │   └── usual_train_new.txt
│       └── sina_news_gbk
│           ├── 2016-02.txt
│           ├── 2016-04.txt
│           ├── 2016-05.txt
│           ├── 2016-06.txt
│           ├── 2016-07.txt
│           ├── 2016-08.txt
│           ├── 2016-09.txt
│           ├── 2016-10.txt
│           ├── 2016-11.txt
│           └── README.txt
└── src
    ├── SMP_first_dict.json
    ├── SMP_freq2_dict.json
    ├── SMP_freq3_dict.json
    ├── SMP_gen_2&3.py
    ├── SMP_p2c_dict.json
    ├── SMP_single_dict.json
    ├── args.py
    ├── check.py
    ├── load.py
    ├── p2c_gen.py
    ├── pinyin.py
    ├── process.py
    ├── process_part.py
    ├── save.py
    ├── settings.py
    ├── sina_first_dict.json
    ├── sina_freq2_dict.json
    ├── sina_freq3_dict.json
    ├── sina_gen.py
    ├── sina_gen3.py
    ├── sina_p2c_dict.json
    └── sina_single_dict.json

然后进入src，依次执行“python sina_gen3.py”生成sina_freq3_dict.json，“python SMP_gen_2&3.py”生成SMP_p2c_dict.json、SMP_freq2_dict.json、SMP_first_dict.json、SMP_single_dict.json、SMP_freq3_dict.json，最后同上“python pinyin.py”即可

## 联系方式

yzr21@mails.tsinghua.edu.cn