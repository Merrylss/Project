from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Store(models.Model):
    """
    店铺类
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='店铺名称')
    cover = models.ImageField(upload_to='static/images/stores/', default='static/images/stores/default.jpg', verbose_name='店铺封面')
    # 店铺状态 1（正常） 0（关闭） 2（删除）
    status = models.IntegerField(default=1, verbose_name='店铺状态')
    intro = models.TextField(verbose_name='店铺介绍')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='开店时间')

    # 关联外键
    user = models.ForeignKey(User, on_delete=models.CASCADE)

