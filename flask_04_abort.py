# coding=utf-8


from flask import Flask,abort

app = Flask(__name__)

#abort
@app.route('/')
def hello_world():
    # 遇到异常抛出错误
    abort(500)
    return 'hello flask'

# 异常捕获
@app.errorhandler(500)
def page_not_found(error):
    return 'This page does not exist', 500


if __name__ == '__main__':
    app.run(debug=True)