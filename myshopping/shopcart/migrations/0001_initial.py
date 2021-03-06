# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-21 07:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopCart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.IntegerField(default=1, verbose_name='购买数量')),
                ('total', models.FloatField()),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户')),
            ],
        ),
    ]
