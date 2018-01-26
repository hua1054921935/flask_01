# coding=utf-8
# coding=utf-8

from flask import Flask,make_response

app = Flask(__name__)

# 请求钩子
@app.route('/')
def hello_world():
    # 这是正在请求的函数
    return 'hello flask'

@app.route('/app')
def hello_flask():
    return 'hello'

# 在处理第一个请求前运行。
@app.before_first_request
def before_first_request():
    print 'before_first_request'



#在每次请求前运行。
@app.before_request
def before_request():
    print 'before_request'


# 如果没有未处理的异常抛出，在每次请求后运行。
@app.after_request
def after_request(response):
    print 'after_request'
    response.headers['Content-Type'] = 'application/json'
    return response

# 在每次请求最后运行，即使有未处理的异常抛出。 可以捕获到异常信息
@app.teardown_request
def teardown_request(e):
    print 'teardown_request %s' % e


if __name__ == '__main__':
    app.run(debug=True)