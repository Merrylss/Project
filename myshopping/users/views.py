import os
import random
import http.client
import urllib.parse


from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
# django系统内置的用户类模块
from django.contrib.auth.models import User
# 系统内置的登录模块 authenticate:身份认证
from django.contrib.auth import authenticate, login, logout
# 内置函数、用户登录才能访问
from django.contrib.auth.decorators import login_required
# 事务管理
from django.db import transaction
from django.http.response import JsonResponse


from . import models
# 请求的路径
host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"
# 用户名是登录ihuyi.com账号名
account = "C76038540"
# 密码 查看密码请登录用户中心->验证码、通知短信->帐户及签名设置->APIKEY
password = "9ec6e4ed7e1d64effc8f589a6065ee23"


# 该函数具有原子性
@transaction.atomic
def user_register(request):
    """
    用户注册
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'users/register.html', {'error_msg': '欢迎注册！'})
    elif request.method == 'POST':
        # 获取表单数据
        username = request.POST['username']
        password = request.POST['password']
        con_password = request.POST['con_password']
        nickname = request.POST['nickname']
        phone = request.POST['mobile']
        code = request.POST['code']

        # 设置原点
        s_id = transaction.savepoint()

        # 判断账号是否可用
        try:
            User.objects.get(username=username)
            return render(request, 'users/register.html', {'error_code': -1, 'error_msg': '账号已经存在！'})
        except:
            # 判断昵称是否可用
            try:
                # User.userinfo.objects.get(nickname=nickname)
                models.UserInfo.objects.get(nickname=nickname)
                return render(request, 'users/register.html', {'error_code': -2, 'error_msg': '昵称已经存在！'})
            except Exception as e:
                print(e)
                # 判断密码
                if password != con_password:
                    return render(request, 'users/register.html', {'error_code': -3, 'error_msg': '两次输入的密码不一致，请重新输入！'})
                if len(password)<6 and len(password)>15:
                    return render(request, 'users/register.html', {'error_code': -4, 'error_msg': '密码要求为6~15位！'})

                try:
                    messgage_code = request.session['message_code']
                except:
                    return render(request, 'users/register.html', {'error_code': -6, 'error_msg': '请获取验证码！'})

                if messgage_code == code:
                    try:
                        user = User.objects.create_user(username=username, password=password)
                        # 创建扩展用户资料
                        user_info = models.UserInfo(nickname=nickname, phone=phone, gender='待完善', user=user)
                        # 保存数据
                        user.save()
                        user_info.save()
                        transaction.savepoint_commit(s_id)
                        return render(request, 'users/login.html', {'error_code': 1, 'error_msg': '账号注册成功!'})
                    except:
                        transaction.savepoint_rollback(s_id)
                        return render(request, 'users/register.html', {'error_code': -4, 'error_msg': '账号注册失败'})
                else:
                    return render(request, 'users/register.html', {'error_code': -5, 'error_msg': '验证码错误'})


def user_login(request):
    """
    用户登录视图函数
    :param request:
    :return:
    """
    if request.method == 'GET':
        # 登陆之后要访问的路径
        try:
            next_url = request.GET['next']
            # print(next_url)
        except:
            next_url = '/'
        return render(request, 'users/login.html', {'next_url': next_url, 'error_msg': '请登陆'})

    elif request.method == 'POST':
        # 获取数据
        username = request.POST['username']
        password = request.POST['password']
        # 下一个跳转的路径
        next_url = request.POST['next_url']
        # print(next_url)
        # 判断验证登录
        user = authenticate(username=username, password=password)
        # print(user)   # TODO 当is_active为False怎么获取不到用户？
        if user is not None:
            # 账号是否锁定
            if user.is_active:
                if next_url == '':
                    next_url = '/'
                # 记录登录状态
                login(request, user)
                return redirect(next_url)
                # return render(request, 'users/login.html', {'error_code': 0, 'error_msg': '登陆成功！'})
            else:
                return render(request, 'users/login.html', {'error_code': -2, 'error_msg': '账号被锁定'})

        else:
            return render(request, 'users/login.html', {'error_code': -1, 'error_msg': '账号或密码错误！请重新登录！'})


@login_required
def user_logout(request):
    """
    用户退出
    :param request:
    :return:
    """
    logout(request)
    return render(request, 'users/login.html', {'error_code': 1, 'error_msg': '账号已经退出！'})
    # return redirect('users/login.html', {'error_code': 1, 'error_msg': '账号已经退出！'})


@login_required
@transaction.atomic
def user_info(request, **kwargs):
    """
    用户信息，可修改
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'users/user_info.html', {})
    elif request.method == 'POST':
        try:
            nickname = request.POST['nickname']
            header = request.FILES['header']
            phone = request.POST['phone']
            gender = request.POST['gender']
            email = request.POST['email']
            print(gender)

            # 设置原点
            s_id = transaction.savepoint()

            try:
                request.user.userinfo.nickname = nickname
                request.user.userinfo.header = header
                request.user.userinfo.phone = phone
                request.user.userinfo.gender = gender
                request.user.email = email
                request.user.save()
                request.user.userinfo.save()
                transaction.savepoint_commit(s_id)
                return render(request, 'users/user_info.html', {'error_code': 1, 'error_msg': '资料完善成功！'})
            except:
                transaction.savepoint_rollback(s_id)
                return render(request, 'users/user_info.html', {'error_code': -1, 'error_msg': '资料完善失败！'})
        except:
            return render(request, 'users/user_info.html', {'error_code': 1, 'error_msg': '资料完善成功！'})


@login_required
def add_address(request):
    """
    添加地址
    :param request:请求头对象
    :return:
    """
    if request.method == 'GET':
        return render(request, 'users/add_address.html', {})
    elif request.method == 'POST':
        consignee = request.POST['consignee']
        phone = request.POST['phone']
        province = request.POST['province']
        city = request.POST['city']
        country = request.POST['country']
        street = request.POST['street']
        intro = request.POST['intro']
        try:
            set_default = request.POST['set_default']
            print(set_default)
            address_list = models.Address.objects.filter(user=request.user)
            for addr in address_list:
                addr.is_default = False
                addr.save()
            address = models.Address(consignee=consignee, phone=phone, province=province, city=city, country=country, street=street,\
                                     intro=intro, is_default=True, user=request.user)
        except:
            address = models.Address(consignee=consignee, phone=phone, province=province, city=city, country=country,
                                     street=street, intro=intro, is_default=False, user=request.user)
        address.save()
        return redirect(reverse('users:address_list'))


@login_required
def delete_address(request, addr_id):
    """
    删除地址
    :param request:请求头对象
    :param addr_id:地址id
    :return:
    """
    addr = models.Address.objects.get(pk=addr_id)
    addr.delete()
    return redirect(reverse("users:address_list"))


@login_required
def address_list(request):
    """
    地址列表
    :param request:
    :return:
    """
    _address_list = models.Address.objects.filter(user=request.user)
    return render(request, 'users/address_list.html', {'address_list': _address_list})


def send_message(request):
    """
    短信验证
    :param request: 请求头对象
    :return:
    """
    """发送信息的视图函数"""
    # 获取ajax的get方法发送过来的手机号码
    mobile = request.GET.get('mobile')
    print(mobile)
    # 通过手机去查找用户是否已经注册
    user = models.UserInfo.objects.filter(phone=mobile)
    if len(user) == 1:
        return JsonResponse({'msg': "该手机已经注册"})
    # 定义一个字符串,存储生成的6位数验证码
    message_code = ''
    for i in range(6):
        i = random.randint(0, 9)
        message_code += str(i)
    # 拼接成发出的短信
    text = "您的验证码是：" + message_code + "。请不要把验证码泄露给其他人。"
    print(text)
    # 把请求参数编码
    params = urllib.parse.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
    # 请求头
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    # 通过全局的host去连接服务器
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    # 向连接后的服务器发送post请求,路径sms_send_uri是全局变量,参数,请求头
    conn.request("POST", sms_send_uri, params, headers)
    # 得到服务器的响应
    response = conn.getresponse()
    # 获取响应的数据
    response_str = response.read()
    # 关闭连接
    conn.close()
    # 把验证码放进session中
    request.session['message_code'] = message_code
    print(eval(response_str.decode()))
    # 使用eval把字符串转为json数据返回
    return JsonResponse(eval(response_str.decode()))