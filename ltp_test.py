#! _*_ encoding=utf-8 _*_

from ltp import LTP

if __name__ == '__main__':
    # http://ltp.ai/docs/index.html

    # 默认加载 Small 模型
    ltp = LTP()
    seg, hidden = ltp.seg(["咱们今天晚上吃什么啊。如果你是第一次使用LTP，不妨花一些时间了解LTP能帮你做什么。",
                           "LTP提供了一系列中文自然语言处理工具，用户可以使用这些工具对于中文文本进行分词、词性标注、句法分析等等工作。",
                           "针对单一自然语言处理任务，生成统计机器学习模型的工具",
                           "针对单一自然语言处理任务，调用模型进行分析的编程接口",
                           "系统可调用的，用于中文语言处理的模型文件",
                           "针对单一自然语言处理任务，基于云端的编程接口",
                           "如果你的公司需要一套高性能的中文语言分析工具以处理海量的文本，或者你的在研究工作建立在一系列底层中文自然语言处理任务之上，"
                           "或者你想将自己的科研成果与前沿先进工作进行对比，LTP都可能是你的选择。"])
    print('seg: %s' % seg)
