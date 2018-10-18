from django.db import models
# 导入django框架内置的用户模块
from django.contrib.auth.models import User


class UserInfo(models.Model):
    '''
    定义用户扩展数据类型
    和系统内置的用户关联
    '''

    # 定义扩展属性字段
    id = models.AutoField(primary_key=True)
    header = models.ImageField(upload_to='static/images/headers/', default='static/images/headers/default.jpg')
    nickname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=5)

    # 和系统内置用户关联
    user = models.OneToOneField(User, on_delete=models.CASCADE)
