from pip._vendor.msgpack.fallback import xrange
import csv

from . import dbmode
from .spider import spider


class lj_spider(spider):
    def __init__(self, **params):
        super().__init__(**params)
        self.filepath = params['filepath']
        self.fieldnames = params['fieldnames']
        self.db: dbmode.db_mode = params['db'] if 'db' in params else None

    def execute(self):
        super().execute()
        print('lj_spider is active')

    # 实现spider数据保存模式
    def _save_data_csv(self, page_num):
        k = int(str(page_num / 5).split(".")[0])
        file_csv = self.filepath + '-' + str(k) + ".csv"
        with open(file_csv, "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()  # 输入表头
            rows = self._get_rows()  # 组织需要写入csv的数据
            writer.writerows(rows)  # 将当前行的数据写入csv文件中
            print("写入" + file_csv + "共" + str(len(rows)) + "条数据\n\n")

    def _get_rows(self):
        count = len(self.container['houseInfo']) + 1
        rows = []
        for i in xrange(1, count):
            content = []  # 定义一个列表行
            for name in self.fieldnames:
                content.append(next(self.data_iterators[name]))  # 执行每列数据的迭代器，取出当前行所对应的值
            if self.data_mode == 'csv':
                row = dict(zip(self.fieldnames, content))  # 将列表行对应到各个字段上，组成一个字典，作为一行数据
                rows.append(row)
            else:
                rows.append(tuple(content))

        return rows

    def _save_data_db(self, page_num):
        rows = self._get_rows()
        self.db.insert(self.fieldnames, rows)
