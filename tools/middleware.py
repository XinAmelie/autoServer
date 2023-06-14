# -*- coding:utf-8 -*-
""""
============================
Time : 2022/11/26 22:38
Author : 王新科
File : middleware.py
software : PyCharm
============================
"""

# 捕获jwt_response_payload_error_handler 的错误信息，并且篡改信息


import json

class ExceptionChange:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        if hasattr(response, 'data'):
            data = response.data
            if isinstance(data, dict):
                data = response.data
            else:
                data = json.loads(json.dumps(data))   # 转化为json可识别的
                print(type(data))
                data = data[0]
            if "non_field_errors" in data.keys():
                if data['non_field_errors'] == ["Unable to log in with provided credentials."]:
                    del response.data['non_field_errors']
                    response.data['msg'] = '用户名或者密码错误'
                    response.data['status'] = '400'
                    response.data['error'] = 'false'
            elif "detail" in data.keys():
                del response.data["detail"]
                response.data["status"] = response.status_code
                response.data["msg"] = "请先登录系统"
        return response
