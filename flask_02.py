# coding=utf-8

from flask import Flask,request

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def hello_world():
    # request的用法
    print 'method: %s' % request.method
    print 'headers: %s' % request.headers
    print 'url: %s' % request.url
    print 'cookies: %s' % request.cookies

    # args: name=XXX  form:name=XXX data=XXX file=图片

    print 'args: %s' % request.args.get('name')
    print 'form: %s' % request.form.get('name')
    print 'data: %s' % request.data
    print 'files: %s' % request.files
    image_files=request.files.get('6')
    image_files.save('./image.jpg')
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')