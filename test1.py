#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 9:54
# @Author  : Weiqiang.long
# @Site    : 
# @File    : test1.py
# @Software: PyCharm
import json
from flask import Flask, Response, render_template, request

app = Flask(__name__)


@app.route("/getossurl", methods=['POST', 'GET'])
def geta():

    a = "312"
    code = '00'
    msg = u'成功'
    # b.update((a))
    # print(b)
    if request.method == "POST":
        path = request.form.get('path')
        times = request.form.get('times')
        times = int(times)
        res = {
            "code": code,
            "msg": msg,
            "url": a
        }
        # json_data = json.dumps(res)
        return Response(json.dumps(res), mimetype='application/json')
# json_data = json.dumps(b)
# print(type(json_data))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)