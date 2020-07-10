import csv

import requests
from lxml import etree
import time

from pip._vendor.msgpack.fallback import xrange

from DFSpider.parser import parser


class spider:
    def __init__(self, **params):
        self.url = params['url']
        self.iterators = {}  # 数据列迭代器map
        self.data_mode = params['data_mode']  # 数据保存模式
        self.mode_fns = {}
        self.type = "Spider"
        self.container = dict()  # 装载页面内容
        self.ps = params['ps']  # 解析器
        self.headers = params['headers']
        self._def_mode_init()

    # 执行爬虫的入口
    def execute(self):
        for i in xrange(1, 21):
            url_str: str = self.url.format(i)  # 构造请求url
            rsp = requests.get(url_str, headers=self.headers)
            self.container = self.ps.parse_content_rsp(rsp)  # 调用解析器获取响应的数据，返回一个数据容器
            self.data_filter()
            self.mode_fns[self.data_mode](i)  # 根据爬虫设置的数据保存模式执行指定函数

    # 加载默认的数据保持模式
    def _def_mode_init(self):
        self.mode_fns['csv'] = self._save_data_csv
        self.mode_fns['db'] = self._save_data_db

    # 自定义数据模式
    def add_mode(self, data_mode: str, mode_fn):
        self.mode_fns[data_mode] = mode_fn

    def data_filter(self):
        for k in self.container:
            print("创建迭代器:\t" + k)
            self.iterators[k] = self.iterator(k, self.container[k])
        print("所有迭代器创建完成\n\n")

    def iterator(self, k, content):
        for i in xrange(len(content)):
            yield self.container[k][i]

    def _save_data_db(self, page_num):
        pass

    def _save_data_csv(self, page_num):
        pass
