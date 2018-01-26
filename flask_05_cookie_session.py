# coding=utf-8
# coding=utf-8

from flask import Flask,make_response,request,session

app = Flask(__name__)
app.config['SECRET_KEY']='hehe'

@app.route('/')
def hello_world():

    return 'hello flask'


@app.route('/set_cookie', methods=['GET', 'POST'])
def set_cookie():
    response=make_response('set_cookie')
    response.set_cookie('name','短语',max_age=3600)

    return response
@app.route('/get_cookie', methods=['GET', 'POST'])
def get_cookie():
    print request.cookies.get('name')
    return 'get_cookie'

@app.route('/delete_cookie', methods=['GET', 'POST'])
def delete_cookie():
    response = make_response('delete_cookie')
    response.delete_cookie('name')
    return response

# session设置 需要设置secret_key
# falsk 设置session是以加密的形式存到浏览器
@app.route('/set_session', methods=['GET', 'POST'])
def set_session():
    session['names']='heima'
    return 'set_session'
# 获取session
@app.route('/get_session', methods=['GET', 'POST'])
def get_session():
    return session.get('names')


if __name__ == '__main__':
    app.run(debug=True)