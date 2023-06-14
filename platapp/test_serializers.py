from django.test import TestCase
from platapp.serializers.auth import LoginSerializer
from platapp.models.auth import User
from django.contrib import auth

from faker import Faker


class TestLoginSerializer(TestCase):
    faker = Faker(locale='zh_CN')

    comName = faker.company()
    num = faker.phone_number()

    # user1 = User.objects.create_user(username='user_test', email='12289000@qq.com', password='111111', realname='你好',
    #                                  phone='18537768419', user_type=1)
    # user2 = User.objects.create_user(username='user444', email='12289000@qq.com', password='111111', realname='你好',
    #                                  phone='18537768413', user_type=1)
    user2 = User.objects.create_user(username=comName, email='12289000@qq.com', password='111111', realname='你好',
                                     phone=num, user_type=1)
    # user3 = User.objects.create(username='user4441', email='12289000@qq.com', password='111111', realname='你好',
    #                             phone='18537768415', user_type=1)

    data = {'username': '和泰网络有限公司', 'password': 111111}
    serializer = LoginSerializer(data=data)
    # print(serializer)
    # user = auth.authenticate(**data)
    # print(user)
    # serializer1 = LoginSerializer(User.objects.all(), many=True)
    # user2 = LoginSerializer(User.objects.filter(username='user444'))
    # print(serializer)
    # print(serializer1.data)
    # print(user2)
    # print(serializer.data)
    print(serializer.is_valid())
    print(serializer.validated_data)
    print(serializer.data)
