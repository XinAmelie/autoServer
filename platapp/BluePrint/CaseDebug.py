# -*- coding:utf-8 -*-
""""
============================
Time : 2022/12/2 22:03
Author : 王新科
File : CaseDebug.py
software : PyCharm

单接口的cas的模块；就像postman
利用form组件去写;定义校验的字段以及actions
============================
psm
branch
env
func_name
psm
request
rpc_context
zone
============================
"""

from django import forms
from enum import Enum,unique
import requests
import urllib3
from rest_framework.exceptions import APIException,ParseError
import json



urllib3.disable_warnings()


'''
enum 不允许在类外直接修改枚举项的值。
unique保证枚举值是唯一不重复的

'''

class CaseDebugForm(forms.Form):

    # 定义需要检验字段的类型
    psm = forms.CharField(min_length=5,max_length=20,strip=True,required=False,label='服务名称')
    branch = forms.CharField(min_length=5,max_length=20,strip=True,required=False,label='分支')
    env = forms.CharField(min_length=3,max_length=20,required=True,label='环境')
    funcName = forms.URLField(max_length=200,required=True,label='接口url')
    request = forms.CharField(strip=True,required=False,min_length=5,label='json代码的内容')
    rpcContext = forms.CharField(strip=True,required=False,label='header头部的信息')
    zone = forms.CharField(strip=True,required=False,label='区域')
    methods = forms.CharField(strip=True,required=True,label='请求方法')

    def fetch_pars(self,formdata):
        '''提取参数'''
        self.formdata = formdata
        methods = self.formdata .get('methods', None)
        psm = self.formdata.get('psm',None)
        env = self.formdata.get('env',None)
        funcName = self.formdata.get('funcName',None)
        request = self.formdata.get('request',None)
        rpcContext = self.formdata.get('rpcContext',None)
        zone = self.formdata.get('zone',None)
        res = [methods,psm,env,funcName,request,rpcContext,zone]
        return res


class Case():
    '''
    case类；定义actions
    '''
    def __init__(self, methods, psm=None, env=None, funcName=None, request=None, rpcContext=None,zone=None):
        self.methods = CaseMethodEnum[methods].name   # 请求方式
        self.psm = psm
        self.branch = None
        self.env = env
        self.func_name = funcName
        self.request = request
        self.rpc_context = rpcContext
        self.zone = zone
        self.result = {}

    def str_to_dict(self):
        '''定义转换类型的action'''
        print('执行了吗？')
        self.rpc_context = {it['key']: it['value'] for it in self.rpc_context} # headers的值
        print(self.rpc_context)
        self.rpc_context = None if self.rpc_context == {'':''} else self.rpc_context
        return self.rpc_context

    @property
    def method(self):
        return CaseMethodEnum(self.methods).value

    # 用例调试，单接口
    def case_debug(self):
        # 数据类型转换
        try:
            res = self.method_request()
        except Exception as e:
            raise ParseError({"参数值有误"})
        # 获取json或者text的结果；后面可以利用它断言
        cur_res = self.get_result(res)
        return cur_res


    def method_request(self):
        res = None
        if self.methods == CaseMethodEnum.GET.name:
            res = self.get_request()
        elif self.methods == CaseMethodEnum.POST.name:
            res = self.post_request()
        elif self.methods == CaseMethodEnum.PUT.name:
            res = self.put_request()
        elif self.methods == CaseMethodEnum.DELETE.name:
            res = self.delete_request()
        return res


    def get_request(self):
        s = requests.session()
        # s.trust_env = False  # 取消环境校验
        proxies = {"http": None, "https": None}
        self.rpc_context  = self.str_to_dict()
        print(f'headers{self.rpc_context }')
        res = s.get(url = self.func_name,params=self.branch,headers=self.rpc_context,proxies=proxies,verify=False)
        return res

    def post_request(self):
        pass

    def put_request(self):
        pass

    def delete_request(self):
        pass

    '''
           elapsed里面几个方法介绍

           total_seconds 总时长，单位秒

           days 以天为单位

           microseconds (>= 0 and less than 1 second) 获取微秒部分，大于0小于1秒

           seconds Number of seconds (>= 0 and less than 1 day) 秒，大于0小于1天

           max = datetime.timedelta(999999999, 86399, 999999) 最大时间

           min = datetime.timedelta(-999999999) 最小时间

           resolution = datetime.timedelta(0, 0, 1) 最小时间单位
           
           设置超时的时长: 
           r = requests.get("http://cn.python-requests.org/zh_CN/latest/", timeout=1)   1s超时
           
           '''
    def get_result(self,res):
        # 也可以获得其他的结果，也可以作为结果返回给前端展示
        status_code = res.status_code
        try:
            # 含有中文的时候取消ensure_ascii
            body = json.dumps(res.json(),ensure_ascii=False)
        except Exception as e:
            body = res.text
            print(f'这个消息体{body}')
        result = {
            'statusCode': status_code,
            'body': body,
            # 'text': res.text,
            'headers': res.headers,
            # 'cookies': res.cookies,
            'encoding': res.encoding,
            'totalSeconds': res.elapsed.total_seconds()  # 耗时几秒
        }
        self.result = result
        return result


class CaseMethodEnum(Enum):
    GET = 1
    POST = 2
    PUT = 3
    DELETE = 4

    @classmethod
    def data(cls):
        return {
            cls.GET.value: cls.GET.name,
            cls.POST.value: cls.POST.name,
            cls.PUT.value: cls.PUT.name,
            cls.DELETE.value: cls.DELETE.name
        }



if __name__ == '__main__':
    print(CaseMethodEnum.data())
    print(CaseMethodEnum.GET.value)
    print(CaseMethodEnum.GET.name)

    print(CaseMethodEnum(1))
    print(CaseMethodEnum['GET'].name)





