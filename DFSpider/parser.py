import abc


class parser(metaclass=abc.ABCMeta):
    def __init__(self):
        print("parser is init")
        self.type = "Parser"

    @abc.abstractmethod
    def execute(self, url):
        pass

    @abc.abstractmethod
    def parse_content_rsp(self, rsp) -> dict:
        pass

