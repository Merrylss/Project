import os
from django.db import models
# 导入django框架内置的用户模块
from django.contrib.auth.models import User


class UserInfo(models.Model):
    """
    定义用户扩展数据类型
    和系统内置的用户关联
    """

    # 定义扩展属性字段
    id = models.AutoField(primary_key=True, verbose_name='用户编号')
    header = models.ImageField(upload_to='static/images/headers/', default='static/images/headers/default.jpg', verbose_name='用户头像')
    nickname = models.CharField(max_length=50, verbose_name='用户昵称')
    phone = models.CharField(max_length=20, verbose_name='用户电话')
    age = models.IntegerField(default=0, verbose_name='用户年龄')
    gender = models.CharField(max_length=5, verbose_name='用户性别')

    # 和系统内置用户关联
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        # 末尾不加s
        verbose_name_plural = '用户'
        # 末尾加s
        # verbose_name = '用户'


class Address(models.Model):
    """
    收货地址
    """
    id = models.AutoField(primary_key=True)
    consignee = models.CharField(max_length=50, verbose_name='收货人')
    phone = models.CharField(max_length=20, verbose_name='收货人电话')
    nation = models.CharField(max_length=50, default='中国', verbose_name='国家')
    province = models.CharField(max_length=50, verbose_name='省')
    city = models.CharField(max_length=50, verbose_name='市区')
    country = models.CharField(max_length=50, verbose_name='县区')
    street = models.CharField(max_length=50, verbose_name='街道')
    intro = models.TextField(verbose_name='详细地址')
    is_default = models.BooleanField(default=False, verbose_name='地址状态')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
