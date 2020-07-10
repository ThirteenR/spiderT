from DFSpider.lianjia_spider import lianjia_spider
from DFSpider.xpath_parser import xpath_parser
from DFSpider.spider_conf import conf

if __name__ == "__main__":
    conf = conf("DFSpider/spider.yaml")  # 加载配置文件
    conf_y = conf.conf_y
    conductor = conf_y['xpath']
    url = conf_y['http']['url']
    data_mode = conf_y['data_mode']
    headers = conf_y['http']['headers']
    parse_mode = conf_y['parse_mode']
    fieldnames = conf_y['csv']['fieldnames']
    db = conf_y['db']
    filepath = conf_y['csv']['filepath']

    ps = xpath_parser(conductor)  # 实例化xpath解析器
    # 实例化链家的爬虫，并指定解析规则
    lanjia = lianjia_spider(
        ps=ps,
        url=url,
        data_mode=data_mode,
        headers=headers,
        fieldnames=fieldnames,
        filepath=filepath
    )
    # 执行链家爬虫
    lanjia.execute()
