# -*- coding:utf-8 -*-
""""
============================
Time : 2022/12/3 23:14
Author : 王新科
File : CaseDebug.py
software : PyCharm

caseDebug的视图函数
============================
"""

from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from django.contrib.auth.decorators import login_required
from platapp.BluePrint.CaseDebug import CaseDebugForm,Case
from rest_framework.exceptions import APIException,ParseError


@swagger_auto_schema(methods=['GET','POST','PUT','DELETE'],operation_summary='单接口调试',operation_description='用于postman类型的单接口调试功能')
@api_view(['GET','POST','PUT','DELETE'])
@permission_classes(())
@login_required()
def debug(request, format=None):
    formdata = request.data
    print(formdata)
    form_obj = CaseDebugForm(formdata)
    if form_obj.is_valid():
        arry = form_obj.fetch_pars(formdata)
        case = Case(*arry)
        result = case.case_debug()
        return Response(data={'raw_data': result}, status=status.HTTP_200_OK)
    return Response(data={'msg': 'error', 'code': status.HTTP_400_BAD_REQUEST, 'error': form_obj.errors},
                        status=status.HTTP_400_BAD_REQUEST)




















