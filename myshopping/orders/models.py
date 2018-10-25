from django.db import models
from django.contrib.auth.models import User


class MyOrder(models.Model):
    """
    订单的数据模型
    """
    id = models.AutoField(primary_key=True)
    order_time = models.DateTimeField(auto_now_add=True, verbose_name='下单时间')
    address = models.CharField(max_length=255, verbose_name='收货地址')
    total = models.FloatField(verbose_name='总计金额额')

    user = models.ForeignKey(User, on_delete=models.CASCADE)


class MyOrderItem(models.Model):
    """
    订单中的购物对象模型
    """
    id = models.AutoField(primary_key=True)
    goods_img = models.ImageField(upload_to='static/images/goods/')
    goods_name = models.CharField(max_length=255, verbose_name='商品名称')
    goods_price = models.FloatField(verbose_name='商品价格')
    goods_count = models.IntegerField(verbose_name='购买数量')
    goods_subtotal = models.FloatField(verbose_name='小计金额')

    myorder = models.ForeignKey(MyOrder, on_delete=models.CASCADE)