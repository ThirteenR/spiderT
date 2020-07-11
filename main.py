from DFSpider.dbmode import db_mode
from DFSpider.lj_spider import lj_spider
from DFSpider.xpath_parser import xpath_parser
from DFSpider.spider_conf import conf

'''
 Author: Renshaoqing
 
'''

if __name__ == "__main__":
    conf = conf("DFSpider/lj_yaml.yaml")  # 加载配置文件
    conf_y = conf.conf_y
    conductor = conf_y['xpath']
    url = conf_y['http']['url']
    data_mode = conf_y['data_mode']
    headers = conf_y['http']['headers']
    parse_mode = conf_y['parse_mode']
    fieldnames = conf_y['csv']['fieldnames']
    dbinfo = conf_y['db']['info']
    table = conf_y['db']['table']
    filepath = conf_y['csv']['filepath']

    db = db_mode(**dbinfo)
    db.creat_table(**table)
    ps = xpath_parser(conductor)  # 实例化xpath解析器
    # 实例化链家的爬虫，并指定解析规则
    lj = lj_spider(
        db=db,
        ps=ps,
        url=url,
        data_mode=data_mode,
        headers=headers,
        fieldnames=fieldnames,
        filepath=filepath,
        pg_count=8
    )
    # 执行链家爬虫
    lj.execute()
