# -*- coding:utf-8 -*-
""""
============================
Time : 2022/11/21 22:53
Author : 王新科
File : auth.py
software : PyCharm
============================
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE = (
        (0, '开发'),
        (1, '测试'),
        (2, '运维'),
        (3, '项目经理')
    )

    realname = models.CharField(verbose_name='真实姓名', max_length=30)  # verbose_name就是在后台显示对对应的名称
    phone = models.CharField(verbose_name='手机', max_length=11, unique=True, null=True, blank=True)
    user_type = models.SmallIntegerField(verbose_name='用户类型', choices=USER_TYPE, default=1)
