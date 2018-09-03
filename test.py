#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 9:18
# @Author  : Weiqiang.long
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import json

import oss2
from flask import Flask, render_template, request, Response

app = Flask(__name__)


@app.route("/getossurl", methods=['POST', 'GET'])
def GetOss():
    """
        生成签名URL
        :param path:文件名
        :param time:授权有效期,默认授权有效期为四天
        :return:签名URL
        """
    # MyAccessKeyId = 'LTAIyxkt6Uz6Lmob'
    # MyAccessKeySecret = 'GMr5YsbuwPyiluxnclDTbfBRyWXYGl'
    # MyEndpoint = 'oss-cn-hangzhou.aliyuncs.com'
    # MyBucketName = 'lwq573925242'

    MyAccessKeyId = 'LTAIGtLs9U0rENY6'
    MyAccessKeySecret = 'aXsG49CtClh3LRDlLMbdzReDx1gmrq'
    MyEndpoint = 'oss-cn-hangzhou.aliyuncs.com'
    MyBucketName = 'xjx-files'


    if request.method == "POST":
        path = request.form.get('path')
        times = request.form.get('times')
        # 为path缺失组装一个json
        path_error = {
            "code": 500,
            "msg": "path参数缺失！"
        }
        if path == None:
            return Response(json.dumps(path_error), mimetype='application/json')

        elif times == None:
            times = 4
            # 换算time,用天数乘以86400秒(一天)
            time = times * 86400
            # print(times)
            auth = oss2.Auth(MyAccessKeyId, MyAccessKeySecret)
            bucket = oss2.Bucket(auth, MyEndpoint, MyBucketName)
            oss_url = bucket.sign_url('GET', path, time)
            code = '00'
            msg = u'请求成功'
            dict_data = {
                "code": code,
                "msg": msg,
                "url": oss_url
            }
            return Response(json.dumps(dict_data), mimetype='application/json')

        else:
            # 转换times的数据类型为int
            times = int(times)
            # 换算time,用天数乘以86400秒(一天)
            time = times * 86400
            # print(times)
            auth = oss2.Auth(MyAccessKeyId, MyAccessKeySecret)
            bucket = oss2.Bucket(auth, MyEndpoint, MyBucketName)
            oss_url = bucket.sign_url('GET', path, time)
            code = '00'
            msg = u'请求成功'
            dict_data = {
                "code": code,
                "msg": msg,
                "url": oss_url
            }
            return Response(json.dumps(dict_data), mimetype='application/json')

    if request.method == "GET":
        path = request.args.get('path')
        times = request.args.get('times')
        # 为path缺失组装一个json
        path_error = {
            "code": 500,
            "msg": "path参数缺失！"
        }
        if path == None:
            return Response(json.dumps(path_error), mimetype='application/json')

        elif times == None:
            times = 4
            # 换算time,用天数乘以86400秒(一天)
            time = times * 86400
            # print(times)
            auth = oss2.Auth(MyAccessKeyId, MyAccessKeySecret)
            bucket = oss2.Bucket(auth, MyEndpoint, MyBucketName)
            oss_url = bucket.sign_url('GET', path, time)
            code = '00'
            msg = u'请求成功'
            dict_data = {
                "code": code,
                "msg": msg,
                "url": oss_url
            }
            return Response(json.dumps(dict_data), mimetype='application/json')

        else:
            # 转换times的数据类型为int
            times = int(times)
            # 换算time,用天数乘以86400秒(一天)
            time = times * 86400
            # print(times)
            auth = oss2.Auth(MyAccessKeyId, MyAccessKeySecret)
            bucket = oss2.Bucket(auth, MyEndpoint, MyBucketName)
            oss_url = bucket.sign_url('GET', path, time)
            code = '00'
            msg = u'请求成功'
            dict_data = {
                "code": code,
                "msg": msg,
                "url": oss_url
            }
            return Response(json.dumps(dict_data), mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)