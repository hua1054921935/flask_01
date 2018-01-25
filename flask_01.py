# coding=utf-8
from flask import Flask,render_template,redirect,url_for,json,current_app

from config import Config
# import_name,static_url_path,static_folder的含义
# import_name 模块名 __name__可以换成模块名
app = Flask(__name__,
            static_url_path='/nb',  # 指定在访问的时候, 路径叫什么名, 替换默认的'static'
            static_folder='static1'  # 指定静态资源访问的目录, 一般不需要改动
            )



'''
调试模式的4种方法
'''
# # 调试模式1
# app.config['debug']=True
# # 方法2 加载文件
# app.config.from_pyfile('config.py')
# # 方法3 加载对象
app.config.from_object(Config)
# # 方法4
# app.debug=True

@app.route('/')
def hello_world():
    return render_template('index.html')


# 路由传递参数
# int:转换器转换为所需的类型，无法转换则无法访问
@app.route('/order/<int:order_id>')
def get_id(order_id):

    return '参数为%s' %order_id



# 重定向
@app.route('/redirct')
def df_redirct():
    # redirct重定向
    # return redirect('http://www.baidu.com')
    # url_for的作用是指定重定向要调用的函数，函数名引起来
    # return redirect(url_for('hello_world'))
    print current_app.config.get('MIJI')
    return redirect(url_for('get_id',order_id=666))
# 返回json数据
@app.route('/jsonresponse')
def d_json():
    hello_world={'miji':'天龙八部','smiji':'六卖神剑'}
    # dumps返回json数据
    return json.dumps(hello_world)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5555)
