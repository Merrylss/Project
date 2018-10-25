import xadmin

# Register your models here.
from xadmin import views
from . import models


class GlobalSetting(object):
    site_title = "商城后台管理系统"
    site_footer = "2018@lss.com"
    menu_style = "accordion"


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class UserInfoAdmin(object):
    """
    用户管理类
    """
    list_display = ['nickname']
    list_per_page = 5

    # 增加和修改的属性
    fields = ["nickname"]


xadmin.site.register(models.UserInfo, UserInfoAdmin)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView, BaseSetting)
