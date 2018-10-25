import xadmin

# Register your models here.
from xadmin import views
from . import models


class StoreAdmin(object):
    """
    用户管理类
    """
    list_display = ['name', 'status']
    list_per_page = 5

    # 增加和修改的属性
    fields = ["name", 'status']


xadmin.site.register(models.Store, StoreAdmin)