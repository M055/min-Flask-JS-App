# -*- coding: utf-8 -*-
from flask import  Flask, render_template, request
# Personal python scripts here
from static.scripts.py.pyscripts import *
import threading
import json
lock = threading.Lock()

app = Flask(__name__)


# for CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST') # Put any other methods you need here
    return response


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print('...........................')
        #curr_POST_response = request.form['submit_button'].split('>')
        curr_POST_response = request.form['submit_button']
        print(curr_POST_response)
        print('-------------')
        data = json.loads(curr_POST_response)
        print(data)
        curr_input = int(data['outValue'])
        # RUn python calculation
        curr_python_calc = yetAnotherSquare(curr_input)
        data['pyValue']=curr_python_calc
        #data = {'outValue':curr_input, 'pyValue':str(curr_python_calc), 'sel1':sel1, 'sel2':sel2}

        return render_template('index.html', data=data)
    else:
        data = {'outValue':'...placeholder...', 'sel1':0, 'sel2':0, 'pyValue':'..'}
        return render_template('index.html', data=data)




if __name__ == '__main__':
    app.run(debug=True)
