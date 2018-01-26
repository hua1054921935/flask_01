# coding=utf-8

# 1.导入共用工具类实现路由转换器
from werkzeug.routing import BaseConverter


# 2.
class RegexConverter(BaseConverter):
        # 1重写init方法
    def __init__(self,url_map,*args):
        # 2.调用父类方法
        super(RegexConverter, self).__init__(url_map)
        # 3.修改regex属性
        self.regex=args[0]