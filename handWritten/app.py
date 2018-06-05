#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 23:32:01 2018

@author: vishaalbommena
"""
from flask import Flask,jsonify
from flask import request


app = Flask(__name__)

@app.route('/api/get_messages', methods = ['POST'])
def get_messages():
    json = request.get_json()
    if json['user'] == "larry":
        print("here")
        return jsonify({'messages':['test1', 'test2']})
    return jsonify({'error':'no user found'})

if __name__ == '__main__':
    app.run(debug = True)