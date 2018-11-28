from flask import Flask, render_template, request
from functions import prime_num,square
import os

app = Flask(__name__)

@app.route('/prime', methods=['GET'])
def prime_num_route():
    
    num = request.args.get('num')
    if num is None or not num.isdigit() :
        return render_template('usage.html', error=True)

    res = prime_num(num)
    return render_template('result.html',
        name="Is number a prime?", num=num, res=res)

  
@app.route('/square', methods=['GET'])
def square_route():
    
    num = request.args.get('num')
    if num is None or not num.isdigit():
        return render_template('usage.html', error=True)

    res = square(num)
    return render_template('result.html',
        name="Square", num=num, res=res)


@app.route('/')
def hello_world():
	return render_template('usage.html', error=False)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('usage.html', error=True)

if __name__ == '__main__':
    app.run()
