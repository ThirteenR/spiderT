import yaml

'''
配置文件加载
'''


class conf:
    conf_y = dict()

    def __init__(self, path):
        with open(path, "rb") as y:
            data = yaml.safe_load_all(y)
            self.conf_y = list(data)[0]

    # def format_conf(self, *params: str):
    #     y = ()
    #     for p in params:
    #         s = p.split('.')
    #         t = ''
    #         for i in range(len(s)):
    #             t = s[i]
    #             if i == len(s) - 1:  # 找到最后一个节点
    #                 y += tuple(s[i])
