# coding=utf-8
# coding=utf-8
from werkzeug.routing import  BaseConverter
from flask import Flask
from comment_utils import RegexConverter
app = Flask(__name__)


@app.route('/')
def hello_world():

    return 'hello flask'


# 3.添加到系统中
# converters存放所有的路由转换器：字典
app.url_map.converters['re']=RegexConverter
# 4.直接使用 匹配电话号
@app.route('/user/<re("1[3456789]\d{9}"):userid>')
def hello_flask(userid):
    return 'hello flask %s' %userid



if __name__ == '__main__':
    app.run(debug=True)
