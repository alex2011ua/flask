from flask import Flask
from flask import render_template
import time
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', time=time.asctime(), name = name)

@app.route("/fsum/")
def fsum():

    a = 10
    b = 5

    return ''

if __name__ == '__main__':
    app.run()
