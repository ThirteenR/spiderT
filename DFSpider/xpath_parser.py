import time
from typing import Dict, Any

import requests
from lxml import etree

from DFSpider.parser import parser

'''
xpath解析器
'''


class xpath_parser(parser):
    def __init__(self, conductor: dict):
        self.conductor = conductor
        super().__init__()

    def parse_content_rsp(self, response) -> dict:
        container = {}
        html = etree.HTML(response)
        for k in self.conductor:
            print("将" + k + "数据放入容器")
            container[k] = html.xpath(self.conductor[k])
        print("响应数据装载完成\n\n")
        return container

    def execute(self, url):
        pass
