# coding=utf-8
# coding=utf-8

from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():

    return render_template('extents.html')
# 包含
@app.route('/include', methods=['GET', 'POST'])
def include():
    return render_template('inclue.html')

# 宏的例子
@app.route('/macro', methods=['GET', 'POST'])
def macro():
    return render_template('macro.html')

if __name__ == '__main__':
    app.run(debug=True)