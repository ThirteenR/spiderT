import time
from typing import Dict, Any

import requests
from lxml import etree

from DFSpider.parser import parser


class xpath_parser(parser):
    def __init__(self, conductor: dict):
        self.conductor = conductor
        super().__init__()

    def parse_content_rsp(self, rsp) -> dict:
        time.sleep(2)
        container: Dict[Any, Any] = {}
        response = rsp.content.decode()
        html = etree.HTML(response)
        for k in self.conductor:
            container[k] = html.xpath(self.conductor[k])
        return container

    def execute(self, url):
        pass
