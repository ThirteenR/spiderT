from pip._vendor.msgpack.fallback import xrange
import csv

from . import dbmode
from .spider import spider


class df_spider(spider):
    def __init__(self, **params):
        super().__init__(**params)
        self.filepath = params['filepath']
        self.data_header = params['data_header']
        self.db: dbmode.db_mode = params['db'] if 'db' in params else None

    def execute(self):
        print('lj_spider is active')
        super().execute()

    # 实现spider数据保存模式
    def _save_data_csv(self, page_num):
        super()._save_data_csv(page_num)
        isnew = False
        k = int(str(page_num / 5).split(".")[0])
        file_csv = self.filepath + '-' + str(k) + ".csv"
        try:
            with open(file_csv, "r") as n:
                pass
        except FileNotFoundError as fn:  # 没有找到当前文件
            isnew = True
            print("Create file " + file_csv + ">>>>>")

        with open(file_csv, "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)  # 列表模式写入
            if isnew:
                writer.writerow(self.data_header)  # 输入表头
            rows = self._get_rows()  # 组织需要写入csv的数据
            writer.writerows(rows)  # 将当前行的数据写入csv文件中
            print("写入" + file_csv + "共" + str(len(rows)) + "条数据\n\n")

    def _get_rows(self):
        count = len(list(self.container.values())[0]) + 1
        rows = []
        for i in xrange(1, count):
            content = []  # 定义一个列表行
            for name in self.data_header:
                content.append(next(self.data_iterators[name]))  # 执行每列数据的迭代器，取出当前行所对应的值
            rows.append(tuple(content))
        return rows

    def _save_data_db(self, page_num):
        super()._save_data_db(page_num)
        rows = self._get_rows()
        self.db.insert(self.data_header, rows)
