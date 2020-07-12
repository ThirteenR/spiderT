from DFSpider.dbmode import db_mode
from DFSpider.df_spider import df_spider
from DFSpider.xpath_parser import xpath_parser
from .spider_conf import conf


def run(c: conf):
    conf_y = c.conf_y
    conductor = conf_y['xpath']
    url = conf_y['http']['url']
    data_mode = conf_y['data_mode']
    headers = conf_y['http']['headers']
    data_header = conf_y['data_header']
    dbinfo = conf_y['db']['info']
    table = conf_y['db']['table']
    filepath = conf_y['csv']['filepath']
    pg_count = conf_y['pg_count']
    db = None
    if data_mode == 'db':
        db = db_mode(**dbinfo)  # 实例化数据库模式
        db.creat_table(**table)  # 创建表格，表格存在不创建
    ps = xpath_parser(conductor)  # 实例化xpath解析器
    # 实例化爬虫，并指定解析规则
    sp = df_spider(
        db=db,
        ps=ps,
        url=url,
        data_mode=data_mode,
        headers=headers,
        data_header=data_header,
        filepath=filepath,
        pg_count=pg_count
    )
    # 执行爬虫
    sp.execute()
