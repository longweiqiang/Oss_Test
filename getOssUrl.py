#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 17:26
# @Author  : Weiqiang.long
# @Site    : 
# @File    : getOssUrl.py
# @Software: PyCharm

import urllib
import oss2

# 封装获取oss对象url
def GetOss(path, time=4):
    """
    生成签名URL
    :param path:文件名
    :param time:授权有效期,默认授权有效期为四天
    :return:签名URL
    """


    MyAccessKeyId = 'XXXX'
    MyAccessKeySecret = 'XXXX'
    MyEndpoint = 'XXXX'
    MyBucketName = 'XXXX'

    # 换算time,用天数乘以86400秒(一天)
    times = time * 86400
    # print(times)

    auth = oss2.Auth(MyAccessKeyId,MyAccessKeySecret)
    bucket = oss2.Bucket(auth, MyEndpoint, MyBucketName)
    oss_url = bucket.sign_url('GET', path ,times)
    return oss_url


def GetUrl(url):
    url = url
    # 解码url
    url_org = urllib.unquote(url)
    return url_org




z = 'files/newfiles/20180502/20180502164340_ebol55wkrr_appTh.png'
f = 'files/newfiles/20180502/20180502164400_4ohtq9pr7b_appTh.png'

# 调用GetOss方法
print(GetOss(f))

# # 调用GetUrl方法
# print(GetUrl('http%3A%2F%2Fxjx-files.oss-cn-hangzhou.aliyuncs.com%2Ffiles%2Fnewfiles%2F20180605%2F20180605143610_y1x4l9fvf0_appTh.png%3FExpires%3D1528526171%26OSSAccessKeyId%3DLTAIGtLs9U0rENY6%26Signature%3DzhMcxMyv1HHYf9OwKKqfeXYEhxU%253D'))







