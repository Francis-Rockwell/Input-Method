import settings


# save函数完成对处理结果的写入保存
def save():

    print("正在保存结果")

    for results in settings.outputs:
        for result in results:
            # 一句拼音的不同处理结果之间用空格分开
            settings.OUTPUT_FILE.write(result + " ")
        # 不同句的拼音处理结果换行
        settings.OUTPUT_FILE.write("\n")
    settings.OUTPUT_FILE.close()
