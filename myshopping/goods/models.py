from django.db import models

# Create your models here.
import stores


class GoodsType(models.Model):
    """
    商品类型
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='static/images/goodstype/', default='static/images/goodstype/default.jpg')
    intro = models.TextField()

    parent = models.ForeignKey('self', null=True, blank=True)


class Goods(models.Model):
    """
    商品数据模型
    """
    id = models.AutoField(primary_key=True, verbose_name='商品编号')
    name = models.CharField(max_length=50, verbose_name='商品名称')
    price = models.FloatField(verbose_name='商品价格')
    stock = models.IntegerField(verbose_name='商品库存')
    sales = models.IntegerField(verbose_name="商品销量")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='上架时间')
    intro = models.TextField(verbose_name='商品描述')

    goodstype = models.ForeignKey(GoodsType, on_delete=models.CASCADE, verbose_name='商品类型')
    store = models.ForeignKey(stores.models.Store, on_delete=models.CASCADE, verbose_name='所属商店')


class GoodsImages(models.Model):
    """
    商品图片
    """
    id = models.AutoField(primary_key=True)
    path = models.ImageField(upload_to='static/images/goods/')
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)