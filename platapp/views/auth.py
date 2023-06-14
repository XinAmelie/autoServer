# -*- coding:utf-8 -*-
""""
============================
Time : 2022/11/21 23:50
Author : 王新科
File : auth.py
software : PyCharm
============================
"""

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from platapp.models import User
from platapp.serializers import UserSerializer, RegisterSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
# 接口文档插件
from drf_yasg.utils import swagger_auto_schema
from django.contrib import auth
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated



# 视图函数
# 1）用于序列化时，将模型类对象传入instance参数
# 2）用于反序列化时，将要被反序列化的数据传入data参数
# 实例化序列化器对象 many=True的作用，就是告诉序列化器内部，当前instance的值是一个列表，所以需要循环 all搭配 many=True   first()搭配 many=false




@swagger_auto_schema(methods=['GET'], operation_summary='用户列表', operation_description='该接口主要是用于请求用户的list接口')
@api_view(['GET'])
def user_list(request, format=None):  # request必传    format=None  url的格式 http://xxx.json
    queryset = User.objects.all()  # queryset是查询结果集
    print(queryset)
    serializer = UserSerializer(instance=queryset, many=True)
    # print(repr(serializer))
    return Response(serializer.data)  # 因为序列化后的数据都是放在data中的

# @permission_classes(()) #该接口解除全局认证和全局权限
# @swagger_auto_schema(methods=['GET'], operation_summary='获取某个用户', operation_description='该接口主要是用于获取某个用户的接口')
# @api_view(['GET'])
# def user_detail(request, _id, format=None):
#     try:
#         req_obj = User.objects.get(pk=_id)
#         print(req_obj)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)  # status提供常用http状态码
#
#     serializer = UserSerializer(instance=req_obj)
#     return Response(serializer.data)



from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.views import exception_handler
from rest_framework_jwt.utils import jwt_decode_handler

# 获取登陆的用户的信息
@permission_classes(()) #该接口解除全局认证和全局权限
@swagger_auto_schema(methods=['GET'], operation_summary='获取用户的信息', operation_description='该接口主要是用于登陆后，获取用户的信息接口')
@api_view(['GET'])
def get_user_info(request, format=None):
    if request.method == 'GET':
        # token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Ilx1NTQ4Y1x1NmNmMFx1N2Y1MVx1N2VkY1x1NjcwOVx1OTY1MFx1NTE2Y1x1NTNmOCIsImV4cCI6MTY3MDE1NjUzNCwiZW1haWwiOiIxMjI4OTAwMEBxcS5jb20ifQ.ln8g7n3A7mqDftlzdmOAHh1BoK1jd-n4qWpoUlMZL98'
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_user = jwt_decode_handler(token)
        # # 获取user_id
        user_id = token_user['user_id']
        # 通过序列化器去查询
        try:
            req_obj = User.objects.get(pk = user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)  # status提供常用http状态码
    serializer = UserSerializer(instance=req_obj)
    return Response(serializer.data)


# 注册视图
@api_view(['POST'])
def register(request):
    # 获取序列化器
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():  # 根据序列器和模型字段综合检查数据是否合法
        user = serializer.register()  # 创建用户
        auth.login(request, user)  # 完成用户登录状态设置
        return Response(data={'msg': 'register', 'is_admin': user.is_superuser, 'retcode': status.HTTP_201_CREATED},
                        status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(data={'msg': 'error', 'retcode': status.HTTP_400_BAD_REQUEST, 'error': serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST)


# 登录视图 rf框架不论什么请求都是request.data
from django.views.decorators.csrf import csrf_exempt, csrf_protect

@api_view(['POST'])
@permission_classes(()) #该接口解除全局认证和全局权限      #####这边有坑，一定要把 @permission_classes(())放在 @api_view()下面，才可以
def login(request):
    # 获取登录信息 --序列器
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validate(request.data)
        if user:
            auth.login(request, user)  # 登录存储session信息
            s_dict = serializer.data
            s_dict.pop('password')
            return Response(data={'msg': 'login success','success':'true', 'username': '赵四','user_datd': s_dict}, status=status.HTTP_200_OK)
    return Response(data={'msg': 'error','retcode': status.HTTP_400_BAD_REQUEST, 'error': serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST)


# 登出视图
@api_view(['GET'])
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return Response(status=status.HTTP_302_FOUND, data={'msg': 'logout'})


from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method='GET', operation_summary='用户定制化接口摘要信息', operation_description='用户定制化接口描述信息....')
@api_view(['GET'])
# 用户定制的接口
def customer_api(request):
    return Response(data={"retcode": status.HTTP_200_OK, "msg": "testing..."})
