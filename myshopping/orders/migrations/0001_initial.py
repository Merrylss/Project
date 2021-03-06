# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-22 08:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_time', models.DateTimeField(auto_now_add=True, verbose_name='下单时间')),
                ('address', models.CharField(max_length=255, verbose_name='收货地址')),
                ('total', models.FloatField(verbose_name='总计金额额')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyOrderItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('goods_img', models.ImageField(upload_to='static/images/goods/')),
                ('goods_name', models.CharField(max_length=255, verbose_name='商品名称')),
                ('goods_price', models.FloatField(verbose_name='商品价格')),
                ('goods_count', models.IntegerField(verbose_name='购买数量')),
                ('goods_subtotal', models.FloatField(verbose_name='小计金额')),
                ('myorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.MyOrder')),
            ],
        ),
    ]
