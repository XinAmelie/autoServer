# -*- coding:utf-8 -*-
""""
============================
Time : 2022/11/22 23:36
Author : 王新科
File : exception.py
software : PyCharm
============================
"""
from rest_framework.views import exception_handler
from rest_framework import exceptions

def my_exception_handler(exc, context):  # exceptions.APIException api层面的异常
    '''
    获取标准的错误响应
    exc:异常信息
    context 上下文
    '''
    error_response = exception_handler(exc, context)
    print('走这不了吗？？')
    if error_response:
        if isinstance(exc, exceptions.APIException):
            error_msg = exc.detail
            if error_msg == 'Authentication credentials were not provided.':
                error_msg = error_msg.replace('Authentication credentials were not provided.','请带上token,身份验证不通过')
            elif error_msg == 'Signature has expired.':
                error_msg = error_msg.replace('Signature has expired.','token已经过期了')
                error_response.status_code = 999  # token过期自定义的code   # 3位数内都可以自定义
        else:
            error_msg = exc
            print(error_msg)

        error_response.data = {
            'msg': 'error',
            'code': error_response.status_code,
            'error': str(error_msg)
        }
    return error_response
