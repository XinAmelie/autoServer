# -*- coding:utf-8 -*-
""""
============================
Time : 2022/11/22 0:38
Author : 王新科
File : urls.py
software : PyCharm
============================
"""

from django.urls import path, include
from platapp import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token


# API文档生成器依赖的类
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(  # schema_view的文档视图
    openapi.Info(
        title='AutoPlat APT DOC',  # api页面的标题
        default_version='v1',
        description='AutoPlat接口文档',
        terms_of_service='王新科&宋文强',
        contact=openapi.Contact(email='wangxinke@sqtp.org' + '*' * 10 + 'songwenqiang@sqtp.org',
                                url='https:www.baidu.com'),
        license=openapi.License(name='BSD License')  # 开源证书
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [

    # 用户接口
    path('user/', views.user_list),
    # path('user/<int:_id>', views.user_detail),  # 参数传递的方式 <int:_id>,把参数传递给视图
    path('sys/profile/', views.get_user_info), # 获取用户信息
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swageer-ui'),  # name是url的命名   # 互动模式
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # 文档模式, cache_timeout 缓存时间
    path('customer/', views.customer_api),  # 测试文档效果接口，后期删除
    # 用户
    path('register/', views.register),
    # path('account_login/v3/', views.login),
    path('logout/', views.logout),

    # jwt的认证接口
    # path('api-token-auth/', obtain_jwt_token),
    path('account_login/v3/', obtain_jwt_token),

    # case接口
    path('case/debug/', views.debug)

]

# urlpatterns = format_suffix_patterns(urlpatterns)  # url格式可以   http:// xxx.json
