import requests
from pip._vendor.msgpack.fallback import xrange

import csv

from DFSpider.spider import spider


class lianjia_spider(spider):
    def __init__(self, **params):
        super().__init__(
            ps=params['ps'],
            url=params['url'],
            data_mode=params['data_mode'],
            headers=params['headers']
        )
        self.filepath = params['filepath']
        self.fieldnames = params['fieldnames']
        print(self.fieldnames)

    # 实现spider数据保存模式
    def _save_data_csv(self, page_num):
        k = int(str(page_num / 5).split(".")[0])
        with open(self.filepath + '-' + str(k) + ".csv", "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()  # 输入表头
            for i in xrange(1, len(self.container['houseInfo']) + 1):
                content = []  # 定义一个列表行
                for name in self.fieldnames:
                    content.append(next(self.iterators[name]))  # 执行每列数据的迭代器，取出当前行所对应的值

                row = dict(zip(self.fieldnames, content))  # 将列表行对应到各个字段上，组成一个字典，作为一行数据
                writer.writerow(row)  # 将当前行的数据写入csv文件中
                print("写入第" + str(i) + "行数据")
