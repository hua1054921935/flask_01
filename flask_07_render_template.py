# coding=utf-8
# coding=utf-8

from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    mylist=[1,2,3,4]
    return render_template('template.html',mylist=mylist)


# 自定义过滤器1
# 函数要以do开头
# 自定义过滤器名lreverse
@app.template_filter('lreverse')
def do_list_reverse(list):
    list.reverse(list)
    return list
# # 自定义过滤器法2
# def do_list1_reverse(list):
#     list.reverse()
#     return list
# app.add_template_filter(do_list1_reverse, 'lsreverse')


if __name__ == '__main__':
    app.run(debug=True)