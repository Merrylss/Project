import xadmin

# Register your models here.
from xadmin import views
from . import models


class GoodsAdmin(object):
    """
    商品管理类
    """
    list_display = ['name', 'price', 'stock']
    list_per_page = 5


xadmin.site.register(models.Goods, GoodsAdmin)
