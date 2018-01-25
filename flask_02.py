# coding=utf-8

from flask import Flask

app = Flask('sources')


@app.route('/')
def hello_world():
    SMIJI='里买神剑'

    return 'hello flask'

if __name__ == '__main__':
    app.run(debug=True)