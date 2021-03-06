# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-19 07:26
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
            name='Store',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='店铺名称')),
                ('cover', models.ImageField(default='static/images/stores/default.jpg', upload_to='static/images/stores/', verbose_name='店铺封面')),
                ('status', models.IntegerField(default=1, verbose_name='店铺状态')),
                ('intro', models.TextField(verbose_name='店铺介绍')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='开店时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
