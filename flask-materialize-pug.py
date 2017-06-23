from flask import Flask, request, send_from_directory, jsonify, Response, send_file
from flask_httpauth import HTTPBasicAuth
import pandas as pd
import os, json, joblib, time
import numpy as np

app = Flask(__name__)

def id_generator(size=10):
    import random, string
    chars= string.digits
    return ''.join(random.choice(chars) for _ in range(size))

@app.route("/")
#@auth.login_required
def start():
    #---- remove in production ---------------
    #----this section is for recompiling riotjs tags in each stage
    from subprocess import call
    print ('\033[94mrebuilding riot tags\033[0m')
    call('riot --template pug ./tags "%s/static/js/tags.js"' % (os.getcwd()), shell=True)
    #---- remove in production ---------------

    h = open('index.html').read()
    h = h % (id_generator())
    return h

@app.route('/<staticFile>')
def send_static(staticFile):
    '''serving static files'''
    return send_from_directory('', staticFile)

@app.route('/fonts/<path:path>')
def send_fonts(path):
    '''serving font files'''
    return send_from_directory('static/fonts', path)

@app.route('/css/<path:path>')
def send_css(path):
    '''serving css files'''
    return send_from_directory('static/css', path)

@app.route('/js/<path:path>')
def send_js(path):
    '''serving js files'''
    return send_from_directory('static/js', path)


if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port=5003)
