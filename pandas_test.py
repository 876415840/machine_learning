#! _*_ encoding=utf-8 _*_


import pandas as pd
import pandas_datareader.data as web
import datetime


def data_frame_use():
    s = pd.Series({"a": 1, "b": 2})
    print(s[:2])

    d = pd.DataFrame([[1, 2, 3], [5, 2, 9]], index=['a', 'b'], columns=['one', 'two', 'three'])
    print(d)

    data = {'one': pd.Series([1, 2, 3], index=['a', 'q', 'c']),
            'two': pd.Series([1, 2, 3, 4], index=['a', 'w', 'c', 'd'])}
    df = pd.DataFrame(data)
    print(df)
    print(df['one'])
    print(df.one)
    # 行
    print(df[1:2])
    # loc[行，列]
    print(df.loc[:, ['one', 'two']])
    # 指定某行某列
    print(df.loc['d', 'two'])
    print(df.iloc[2:3, 1:2])
    print(df.iloc[[1, 3], [0, 1]])


def read_csv():
    # header指定哪行作为列索引(默认0)，index_col指定哪列作为行索引
    c = pd.read_csv('/Users/finup/Downloads/导出信息.csv', index_col=0, encoding='utf-8')
    print(c)
    return c


def read_web_info():
    """
    pandas_datareader 是一个远程获取金融数据的Python工具，通过它可以方便获得下面公司和机构的数据：

    1、Facebook Finance 脸书金融
    2、Yahoo! Finance 雅虎金融
    3、Google Finance 谷歌金融
    4、Enigma 一个公共数据搜索的提供商
    5、St.Louis FED(FRED) 圣路易斯联邦储备银行
    6、Kenneth French's data library 肯尼斯弗兰奇资料库
    7、World Bank 世界银行
    8、OECD 经合组织
    9、Eurostat 欧盟统计局
    10、Thrift Savings Plan 美国联邦政府管理离退休的组织
    11、Oanda currency historical rate 外汇经纪商
    12、Nasdaq Trader symbol definitions 纳斯达克
    """
    # 从yahoo网站获取深圳交易所股票'康华生物'，18-1-1到今天的数据
    dr = web.DataReader("300841.SZ", "yahoo", datetime.datetime(2018, 1, 1), datetime.date.today())
    print(dr.columns)
    print(dr.index)
    # 多少行和列
    print(dr.shape)
    return dr


if __name__ == '__main__':
    # DataFrame的基本使用
    # data_frame_use()

    # 读取csv文件并转换
    # read_csv()

    # 读取各个网站股票信息并转换
    df = read_web_info()
    # 前多少行 后多少行
    print(df.head(3))
    print(df.tail(3))
    # 统计情况 最大、最小、标准差等等
    print(df.describe())
    # 每列统计信息，不为空多上行以及类型、整体大小等等
    print(df.info())
    # isnull notnull 返回true、false的矩阵
    # 包含空值的数据
    print(df[df.isnull().T.any()])
    # 条件筛选
    print(df[df.loc[:, 'High'] > 995])
