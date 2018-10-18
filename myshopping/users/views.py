from django.shortcuts import render
# django系统内置的用户类模块
from django.contrib.auth.models import User
# 系统内置的登录模块 authenticate:身份认证
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from . import models

def user_register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html', {})
    elif request.method == 'POST':
        # 获取表单数据
        username = request.POST['username']
        password = request.POST['password']
        con_password = request.POST['con_password']
        nickname = request.POST['nickname']

        # 判断账号是否可用
        try:
            user = User.objects.get(username=username)
            return render(request, 'users/register.html', {'error_code': -1, 'error_msg': '账号已经存在！'})
        except:
            # 判断昵称是否可用
            try:
                user_profile = User.userprofile.objects.get(nickname=nickname)
                return render(request, 'users/register.html', {'error_code': -2, 'error_msg': '昵称已经存在！'})
            except:
                # 判断密码
                if password != con_password:
                    return render(request, 'users/register.html', {'error_code': -3, 'error_msg': '两次输入的密码不一致，请重新输入！'})
                user = User.objects.create_user(username=username, password=password)
                # 创建扩展用户资料
                userinfo = models.UserInfo(nickname=nickname, phone='待完善', gender='待完善', user=user)
                # 保存数据
                user.save()
                userinfo.save()
                return render(request, 'users/register.html', {'error_code': 1, 'error_msg': '账号注册成功！'})


def user_login(request):
    '''
    用户登录试图函数
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'users/user_login.html', {})

    elif request.method == 'POST':
        # 获取数据
        username = request.POST['username']
        password = request.POST['password']

        # 判断验证登录
        user = authenticate(username=username, password=password)

        if user is not None:
            # 用户存在
            
