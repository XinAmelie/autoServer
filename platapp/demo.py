# -*- coding:utf-8 -*-
""""
============================
Time : 2022/12/3 22:38
Author : 王新科
File : demo.py
software : PyCharm

主要用于调试用的脚本
============================
"""

# formdata = {
#             "baranch": "master","env":"prod","func_name":"https://www.baidu.com","psm":"oec.seller.reach","zone":"SGALI",
#             "request":"{\r\n    \"base\": {\r\n        \"Addr\": \"\",\r\n        \"Caller\": \"\",\r\n        \"Client\": \"\",\r\n        \"Extra\": {\r\n            \"\": \"\"\r\n        },\r\n        \"LogID\": \"\",\r\n        \"TrafficEnv\": {\r\n            \"Env\": \"\",\r\n            \"Open\": false\r\n        }\r\n    },\r\n    \"info\": {\r\n        \"app_id\": 0,\r\n        \"locale\": \"\",\r\n        \"mode_type\": 0,\r\n        \"open_platform_locale\": \"\",\r\n        \"params\": [\r\n            {\r\n                \"key\": \"\",\r\n                \"starling_project\": 0,\r\n                \"value\": \"\",\r\n                \"value_type\": 0\r\n            }\r\n        ],\r\n        \"seller_id\": 0,\r\n        \"user_id\": 0,\r\n        \"user_id_type\": 0\r\n    },\r\n    \"op_cfg\": {\r\n        \"extra_info\": {\r\n            \"\": \"\"\r\n        }\r\n    },\r\n    \"task_id\": 0\r\n}",
#             "rpc_context":[{"key": "section three", "value": "22222", "type": "A", "isCheck": "true", "indexData": 0},{"key": "section three1", "value": "222221", "type": "B", "isCheck": "true", "indexData": 1}],
#             "rrr1":""
#             }

# formdata = {'psm': 'oec.seller.reach', 'methods': 'GET', 'funcName': 'http://localhost.charlesproxy.com:8999/api/user/', 'zone': 'SGALI', 'env': 'prod', 'request': '', 'rpcContext': [{'key': 'Authorization', 'value': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Ilx1NTQ4Y1x1NmNmMFx1N2Y1MVx1N2VkY1x1NjcwOVx1OTY1MFx1NTE2Y1x1NTNmOCIsImV4cCI6MTY3MDY5MjE0OCwiZW1haWwiOiIxMjI4OTAwMEBxcS5jb20ifQ.Dv5BEr58o9gFkAlZ1EZhNTUi1phMTeYCzj7Er5wR5LY', 'type': 'A', 'isCheck': True, 'indexData': 0}]}




# a = formdata.get('rrr', 'ooo')
# print(a)

# res = [method, psm, env, func_name, request, rpc_context, zone]

# method = formdata .get('methods', None)
# psm = formdata.get('psm',None)
# env = formdata.get('env',None)
# funcName = formdata.get('func_name',None)
# request = formdata.get('request',None)
# rpcContext =formdata.get('rpcContext',None)
# zone = formdata.get('zone',None)
#
# res = [method,psm,env,funcName,request,rpcContext,zone]

# print(*res)





# print(type(formdata))
#
# print(formdata['rpc_context'])
# head = formdata['rpc_context']
#
#
#
#     # d1 = {(it['x'], it['y']): it['demand'] for it in l1}
#
# d1 = {it['key']: it['value'] for it in head}
# print(*d1.values())
#
# print(d1)

# import json
#
# d = {'a':1,'b':2}
# print(type(d))
#
# a = json.dumps(d)
# print(a)
# print(type(a))

# s = 0.014067
#
# a = s * 1000
# print(a)

# url = 'https://astro-api-boe.bytedance.net/api/v1/data_factory/fulfillment_domain/fulfill_unit/get?main_order_id=576816699778238927&main_order_id=576816699778238927'
# a = url.split('?')[1].split('&')
#
#
# print(a)

# import requests
# import urllib3
# urllib3.disable_warnings()
# s = requests.session()
# # s.trust_env = False # 取消环境校验
# proxies = { "http": None, "https": None}
# head = {
#     'X-Jwt-Token':'eyJhbGciOiJSUzI1NiIsImtpZCI6IiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwYWFzLnBhc3Nwb3J0LmF1dGgiLCJleHAiOjE2NzA2MDI1MzYsImlhdCI6MTY3MDU5ODg3NiwidXNlcm5hbWUiOiJ3YW5neGlua2Uuc2lydWkzNjUiLCJ0eXBlIjoicGVyc29uX2FjY291bnQiLCJyZWdpb24iOiJjbiIsInRydXN0ZWQiOnRydWUsInV1aWQiOiI4OTllZDQ4Yi03ZjdlLTRkOWQtYjBiNS0wZjIyMjg4MGIwNGMiLCJzaXRlIjoib25saW5lIiwic2NvcGUiOiJieXRlZGFuY2UiLCJzZXF1ZW5jZSI6IlRlc3QiLCJvcmdhbml6YXRpb24iOiLkuqflk4HnoJTlj5Hlkozlt6XnqIvmnrbmnoTpg6gt6LSo6YeP5L-d6ZqcLeWbvemZheeUteWVhi3nlLXllYbkuK3lj7AiLCJ3b3JrX2NvdW50cnkiOiJDSE4iLCJhdmF0YXJfdXJsIjoiaHR0cHM6Ly9zMS1pbWZpbGUuZmVpc2h1Y2RuLmNvbS9zdGF0aWMtcmVzb3VyY2UvdjEvdjJfMjA4ODQ4OTItYThkYS00NWJiLTlhMWYtMzQ5OTdiYmI0NDVnfj9pbWFnZV9zaXplPW5vb3BcdTAwMjZjdXRfdHlwZT1cdTAwMjZxdWFsaXR5PVx1MDAyNmZvcm1hdD1wbmdcdTAwMjZzdGlja2VyX2Zvcm1hdD0ud2VicCIsImVtYWlsIjoid2FuZ3hpbmtlLnNpcnVpMzY1QGJ5dGVkYW5jZS5jb20iLCJlbXBsb3llZV9pZCI6ODc1MzcxM30.uA__DhI9ncXfIS619gidZP3fWqjWsMVWXFXuf-AtatKZ6qVr-8tp9Y3jLhuz0UHz_fKqeKpeSgFM0GGop2z-xG018lX-6fDwwoKHi7GuOAU0kdDvxvpKM2ZfFE_m_Xokk0gUI59_J6fs4pKkmkmF-LO3geT-XVdWhvWOkGTimX8'
# }
# url = 'https://astro-api-boe.bytedance.net/api/v1/data_factory/fulfillment_domain/fulfill_unit/get?main_order_id=576816699778238927&main_order_id=576816699778238927'
# a =s.get(url=url,verify=False,headers=head,proxies=proxies)
# print(a.text)
# print(a)


a = {'1':'1'}
print(isinstance(a,dict))
for item in a.keys():
    # print(len(item))
    print(item)
    if len(item):
        a = None

print(a)