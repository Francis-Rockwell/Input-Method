# README

## 项目介绍

​		Replanted course project from my Introduction to AI class

​		本项目为使用马尔科夫方法以及viterbi算法实现的简易拼音输入法。

## 文件结构

. <br />
├── README.md <br />
├── data <br />
│   ├── input.txt <br />
│   ├── output.txt <br />
│   └── std_output.txt <br />
└── src <br />
    ├── SMP_gen_2&3.py <br />
    ├── args.py <br />
    ├── check.py <br />
    ├── load.py <br />
    ├── p2c_gen.py <br />
    ├── pinyin.py <br />
    ├── process.py <br />
    ├── process_part.py <br />
    ├── save.py <br />
    ├── settings.py <br />
    ├── sina_first_dict.json <br />
    ├── sina_freq2_dict.json <br />
    ├── sina_gen.py <br />
    ├── sina_gen3.py <br />
    ├── sina_p2c_dict.json <br />
    └── sina_single_dict.json <br />

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

​		如果要体验附加功能方法一是**从https://cloud.tsinghua.edu.cn/d/70fbb2ae255f44308ecb/ 下载sina_freq3_dict.json、SMP_first_dict.json、SMP_freq2_dict.json、SMP_p2c_dict.json、SMP_single_dict.json共6个文件，将其拷贝到./src中，形成如下结构**，

. <br />
├── README.md <br />
├── data <br />
│   ├── input.txt <br />
│   ├── output.txt <br />
│   └── std_output.txt <br />
└── src <br />
    ├── **SMP_first_dict.json** <br />
    ├── **SMP_freq2_dict.json** <br />
    ├── **SMP_freq3_dict.json** <br />
    ├── SMP_gen_2&3.py <br />
    ├── **SMP_p2c_dict.json** <br />
    ├── **SMP_single_dict.json** <br />
    ├── args.py <br />
    ├── check.py <br />
    ├── load.py <br />
    ├── p2c_gen.py <br />
    ├── pinyin.py <br />
    ├── process.py <br />
    ├── process_part.py <br />
    ├── save.py <br />
    ├── settings.py <br />
    ├── sina_first_dict.json <br />
    ├── sina_freq2_dict.json <br />
    ├── **sina_freq3_dict.json** <br />
    ├── sina_gen.py <br />
    ├── sina_gen3.py <br />
    ├── sina_p2c_dict.json <br />
    └── sina_single_dict.json <br />

后续运行方法和参数同上，且可以通过-t参数选择运行模式

​		方法二是**从https://cloud.tsinghua.edu.cn/d/8712d759def745cb8bae/ 下载语料库.zip和拼音汉字表.zip，解压后放在src文件夹内，形成如下结构：**

. <br />
├── README.md <br />
├── data <br />
│   ├── input.txt <br />
│   ├── output.txt <br />
│   ├── std_output.txt <br />
│   ├── **拼音汉字表** <br />
│   │   ├── README.txt <br />
│   │   ├── 一二级汉字表.txt <br />
│   │   └── 拼音汉字表.txt <br />
│   └── **语料库** <br />
│       ├── SMP2020 <br />
│       │   ├── README.txt <br />
│       │   └── usual_train_new.txt <br />
│       └── sina_news_gbk <br />
│           ├── 2016-02.txt <br />
│           ├── 2016-04.txt <br />
│           ├── 2016-05.txt <br />
│           ├── 2016-06.txt <br />
│           ├── 2016-07.txt <br />
│           ├── 2016-08.txt <br />
│           ├── 2016-09.txt <br />
│           ├── 2016-10.txt <br />
│           ├── 2016-11.txt <br />
│           └── README.txt <br />
└── src <br />
    ├── SMP_first_dict.json <br />
    ├── SMP_freq2_dict.json <br />
    ├── SMP_freq3_dict.json <br />
    ├── SMP_gen_2&3.py <br />
    ├── SMP_p2c_dict.json <br />
    ├── SMP_single_dict.json <br />
    ├── args.py <br />
    ├── check.py <br />
    ├── load.py <br />
    ├── p2c_gen.py <br />
    ├── pinyin.py <br />
    ├── process.py <br />
    ├── process_part.py <br />
    ├── save.py <br />
    ├── settings.py <br />
    ├── sina_first_dict.json <br />
    ├── sina_freq2_dict.json <br />
    ├── sina_freq3_dict.json <br />
    ├── sina_gen.py <br />
    ├── sina_gen3.py <br />
    ├── sina_p2c_dict.json <br />
    └── sina_single_dict.json <br />

然后进入src，依次执行“python sina_gen3.py”生成sina_freq3_dict.json，“python SMP_gen_2&3.py”生成SMP_p2c_dict.json、SMP_freq2_dict.json、SMP_first_dict.json、SMP_single_dict.json、SMP_freq3_dict.json，最后同上“python pinyin.py”即可

## 联系方式

yzr21@mails.tsinghua.edu.cn
