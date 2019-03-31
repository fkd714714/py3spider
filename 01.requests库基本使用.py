#!usr/bin/env python
# -*- coding:utf-8 _*-
""" 
@author:fkd714
@file: 01.requests库基本使用.py 
@time: 2019/02/13 
@python version: 3.7.1
"""  

import requests

'''带参数get请求'''
# data = {'name': 'germey', 'age': 22}
# response = requests.get("http://httpbin.org/get", params=data)
# print(response.text)
#
#
'''解析json'''
# response = requests.get("http://httpbin.org/get")
# print(response.text)
# print(type(response.text))
#
# print(response.json())
# print(type(response.json()))
#
# import json
# print(json.loads(response.text))
#
# # 可见response.json()实际上调用了json.loads()方法
#
#
'''获取二进制数据'''
# response = requests.get("https://github.com/favicon.ico")
# print(type(response.text), type(response.content))
# print(response.text)
# print(response.content)
#
# with open('D:/ProgramProject/python/spider/favicon.ico', 'wb') as f:
#     f.write(response.content)
#     f.close()
#
#
'''添加headers'''
# response = requests.get("https://www.zhihu.com/explore")
# print(response.text)
# # 不添加headers访问知乎报错
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
# response = requests.get("https://www.zhihu.com/explore", headers=headers)
# print(response.text)
#
# #----------------------分隔--------------------------
#
'''基本post请求'''
# data = {'name': 'germey', 'age': '22'}
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
# response = requests.post("http://httpbin.org/post", data=data, headers=headers)
# print(response.text)
# print(response.json())
#
# #---------------------响应-------------------------------
#
'''response属性'''
# response = requests.get('http://www.jianshu.com')
# print(type(response.status_code), response.status_code)
# print(type(response.headers), response.headers)
# print(type(response.cookies), response.cookies)
# print(type(response.url), response.url)
# print(type(response.history), response.history)
#
#
'''状态码判断'''
# response = requests.get('http://www.jianshu.com/hello.html')
# if response.status_code == requests.codes.ok:
#     print("Request Successfully")
# else:
#     print('404 Not Found')
#
# #状态码大全
# 100: ('continue',),
# 101: ('switching_protocols',),
# 102: ('processing',),
# 103: ('checkpoint',),
# 122: ('uri_too_long', 'request_uri_too_long'),
# 200: ('ok', 'okay', 'all_ok', 'all_okay', 'all_good', '\\o/', '✓'),
# 201: ('created',),
# 202: ('accepted',),
# 203: ('non_authoritative_info', 'non_authoritative_information'),
# 204: ('no_content',),
# 205: ('reset_content', 'reset'),
# 206: ('partial_content', 'partial'),
# 207: ('multi_status', 'multiple_status', 'multi_stati', 'multiple_stati'),
# 208: ('already_reported',),
# 226: ('im_used',),
#
# # Redirection.
# 300: ('multiple_choices',),
# 301: ('moved_permanently', 'moved', '\\o-'),
# 302: ('found',),
# 303: ('see_other', 'other'),
# 304: ('not_modified',),
# 305: ('use_proxy',),
# 306: ('switch_proxy',),
# 307: ('temporary_redirect', 'temporary_moved', 'temporary'),
# 308: ('permanent_redirect',
#       'resume_incomplete', 'resume',), # These 2 to be removed in 3.0
#
# # Client Error.
# 400: ('bad_request', 'bad'),
# 401: ('unauthorized',),
# 402: ('payment_required', 'payment'),
# 403: ('forbidden',),
# 404: ('not_found', '-o-'),
# 405: ('method_not_allowed', 'not_allowed'),
# 406: ('not_acceptable',),
# 407: ('proxy_authentication_required', 'proxy_auth', 'proxy_authentication'),
# 408: ('request_timeout', 'timeout'),
# 409: ('conflict',),
# 410: ('gone',),
# 411: ('length_required',),
# 412: ('precondition_failed', 'precondition'),
# 413: ('request_entity_too_large',),
# 414: ('request_uri_too_large',),
# 415: ('unsupported_media_type', 'unsupported_media', 'media_type'),
# 416: ('requested_range_not_satisfiable', 'requested_range', 'range_not_satisfiable'),
# 417: ('expectation_failed',),
# 418: ('im_a_teapot', 'teapot', 'i_am_a_teapot'),
# 421: ('misdirected_request',),
# 422: ('unprocessable_entity', 'unprocessable'),
# 423: ('locked',),
# 424: ('failed_dependency', 'dependency'),
# 425: ('unordered_collection', 'unordered'),
# 426: ('upgrade_required', 'upgrade'),
# 428: ('precondition_required', 'precondition'),
# 429: ('too_many_requests', 'too_many'),
# 431: ('header_fields_too_large', 'fields_too_large'),
# 444: ('no_response', 'none'),
# 449: ('retry_with', 'retry'),
# 450: ('blocked_by_windows_parental_controls', 'parental_controls'),
# 451: ('unavailable_for_legal_reasons', 'legal_reasons'),
# 499: ('client_closed_request',),
#
# # Server Error.
# 500: ('internal_server_error', 'server_error', '/o\\', '✗'),
# 501: ('not_implemented',),
# 502: ('bad_gateway',),
# 503: ('service_unavailable', 'unavailable'),
# 504: ('gateway_timeout',),
# 505: ('http_version_not_supported', 'http_version'),
# 506: ('variant_also_negotiates',),
# 507: ('insufficient_storage',),
# 509: ('bandwidth_limit_exceeded', 'bandwidth'),
# 510: ('not_extended',),
# 511: ('network_authentication_required', 'network_auth', 'network_authentication'),
#
# # ------------------高级操作-------------------------
#
'''文件上传'''
# files = {'file': open('favicon.ico', 'rb')}
# response = requests.post("http://httpbin.org/post", files=files)
# print(response.text)
#
#
'''获取cookie'''
# response = requests.get("https://www.baidu.com")
# print(response.cookies)
# for key, value in response.cookies.items():
#     print(key + '=' + value)
#
#
'''会话维持（用于模拟登陆）'''
# # #以下为错误案例 # #
# requests.get('http://httpbin.org/cookies/set/number/123456789')
# response = requests.get('http://httpbin.org/cookies')
# print(response.text)
#
# # #正确方法 # #
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# response = s.get('http://httpbin.org/cookies')
# print(response.text)
#
#
'''证书验证'''
# # 消除InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. 警告
# import urllib3
# urllib3.disable_warnings()
# # 原来的12306网站证书不安全，会不给访问，可以通过verify=False取消验证，但会报上面的错误，使用urllib3.disable_warnings()会忽略错误
# response = requests.get('https://www.12306.cn', verify=False)
# print(response.status_code)
#
# # #手动导入证书（现在12306已经不需要了）# #
# response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
# print(response.status_code)
#
#
'''代理设置'''
# proxies = {
#   "http": "http://127.0.0.1:9743",
#   "https": "https://127.0.0.1:9743",
# }
# response = requests.get("https://www.taobao.com", proxies=proxies)
# print(response.status_code)
#
# # 如果代理需要设置账户名和密码,只需要将字典更改为如下：
# proxies = {
#     "http": "http://user:password@127.0.0.1:9743/",
# }
#
# # 如果你的代理是通过sokces这种方式则需要pip install "requests[socks]"
# proxies = {
#     'http': 'socks5://127.0.0.1:9742',
#     'https': 'socks5://127.0.0.1:9742'
# }
#
#
'''超时设置'''
# from requests.exceptions import ReadTimeout
# try:
#     response = requests.get("http://httpbin.org/get", timeout=1)
#     print(response.status_code)
# except ReadTimeout:
#     print('Timeout')
#
#
'''认证设置'''
# # 第1种形式
# from requests.auth import HTTPBasicAuth
# r = requests.get('http://120.27.34.24:9001', auth=HTTPBasicAuth('user', '123'))
# # 第2钟形式
# r = requests.get('http://120.27.34.24:9001', auth=('user', '123'))
# print(r.status_code)
#
#
'''异常处理'''
# from requests.exceptions import ReadTimeout, ConnectionError, RequestException
# try:
#     response = requests.get("http://httpbin.org/get", timeout=0.1)
#     print(response.status_code)
# except ReadTimeout:
#     print('Timeout')
# except ConnectionError:
#     print('Connection error')
# except RequestException:
#     print('Error')
#
