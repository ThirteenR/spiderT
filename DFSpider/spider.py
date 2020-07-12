"""
 爬虫基类
 Author : Renshaoqing
"""


class spider:
    def __init__(self, **params):
        self.mode_fns = {'csv': self._save_data_csv, 'db': self._save_data_db}  # 初始化数据模式的函数字典

    # 执行爬虫的入口
    def execute(self):
        pass

    def _request(self, boot):
        pass

    # 自定义数据模式
    def add_data_mode(self, data_mode: str, mode_fn):
        self.mode_fns[data_mode] = mode_fn

    def _data_filter(self):
        pass

    def _save_data_db(self, page_num):
        print("Save data with db mode >>>>>")
        pass

    def _save_data_csv(self, page_num):
        print("Save data with cvs mode >>>>>")
        pass
