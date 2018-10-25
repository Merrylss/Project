from django.db import models
# 导入django框架内置的用户模块
from django.contrib.auth.models import User

import goods


class ShopCart(models.Model):
    """
    购物车模型
    """
    id = models.AutoField(primary_key=True)
    goods = models.ForeignKey(goods.models.Goods, on_delete=models.CASCADE, verbose_name='商品名称')
    count = models.IntegerField(default=10, verbose_name='商品数量')
    total = models.FloatField()
    users = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加购物车时间')
