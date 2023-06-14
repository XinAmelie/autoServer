# -*- coding:utf-8 -*-
""""
============================
Time : 2022/11/26 12:16
Author : 王新科
File : cust_jwt_resposed.py
software : PyCharm

用于 jwt正确返回值的自定义
============================
"""


from platapp.serializers.auth import UserSerializer

# 成功的
def jwt_response_payload_handler(token,user=None,request=None):
    if token:
        return {
            'data': {
                'token': token,
                'userInfo': UserSerializer(user).data
            }
        }


# 错误的
def jwt_response_payload_error_handler(requesu=None):
    return {
        'msg': '用户名或者密码错误，请输入重新输入',
        'code': 400,
        'error': 'false'
    }