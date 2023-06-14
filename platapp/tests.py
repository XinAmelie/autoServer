from django.test import TestCase

# Create your tests here.

# 测试form表单是否是有效的


import os

from platapp.BluePrint.CaseDebug import CaseDebugForm

# 脱离console，需要如此的配置
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','autoServer.settings')
django.setup()


"""
    psm = forms.CharField(min_length=5,max_length=20,strip=True,required=False,label='服务名称')
    branch = forms.CharField(min_length=5,max_length=20,strip=True,required=False,label='分支')
    env = forms.CharField(min_length=5,max_length=20,required=True,label='环境')
    func_name = forms.URLField(max_length=200,required=True,label='接口url')
    request = forms.CharField(strip=True,required=True,min_length=5,label='json代码的内容')
    rpc_context = forms.CharField(strip=True,required=False,label='header头部的信息')
    zone = forms.CharField(strip=True,required=False,label='区域')


"""

# python manage.py test platapp.tests

# 数据源
formdata = {
            "baranch": "master","env":"prod","func_name":"https://www.baidu.com","psm":"oec.seller.reach","zone":"SGALI",
            "request":"{\r\n    \"base\": {\r\n        \"Addr\": \"\",\r\n        \"Caller\": \"\",\r\n        \"Client\": \"\",\r\n        \"Extra\": {\r\n            \"\": \"\"\r\n        },\r\n        \"LogID\": \"\",\r\n        \"TrafficEnv\": {\r\n            \"Env\": \"\",\r\n            \"Open\": false\r\n        }\r\n    },\r\n    \"info\": {\r\n        \"app_id\": 0,\r\n        \"locale\": \"\",\r\n        \"mode_type\": 0,\r\n        \"open_platform_locale\": \"\",\r\n        \"params\": [\r\n            {\r\n                \"key\": \"\",\r\n                \"starling_project\": 0,\r\n                \"value\": \"\",\r\n                \"value_type\": 0\r\n            }\r\n        ],\r\n        \"seller_id\": 0,\r\n        \"user_id\": 0,\r\n        \"user_id_type\": 0\r\n    },\r\n    \"op_cfg\": {\r\n        \"extra_info\": {\r\n            \"\": \"\"\r\n        }\r\n    },\r\n    \"task_id\": 0\r\n}",
            "rpc_context":[{"key": "section three", "value": "22222", "type": "A", "isCheck": "true", "indexData": 0}]
            }
form_obj = CaseDebugForm(formdata)
form_obj.is_valid()
print(form_obj.is_valid())
print(form_obj.cleaned_data)


# form_obj.errors 查看错误的原因

# form_obj.cleaned_data 查看正确的结果

