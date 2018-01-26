# coding=utf-8
# coding=utf-8

from flask import Flask
# 从flask_script扩展中导入Manager
from flask_script import Manager

app = Flask(__name__)
# 创建manager
manager=Manager(app)
app.debug=True

@app.route('/')
def hello_world():

    return 'hello flask'

if __name__ == '__main__':
    # python flask_06_script.py runserver -d只有错误显示没有重新加载服务器
    # -p 端口号 -h ip地址
    manager.run()