from django.conf.urls import url

from . import views

urlpatterns = [
    # 结算确认，检查收货地址
    url(r'order_confirm/$', views.order_confirm, name='order_confirm'),
    # 结算付款
    url(r'order_pay/$', views.order_pay, name='order_pay'),
    # 生成订单
    url(r'order_done/$', views.order_done, name='order_done'),
    # 查看所有订单
    url(r'order_list/$', views.order_list, name='order_list'),
    # 查看单个订单
    url(r'(?P<order_id>\d+)/order_info/$', views.order_info, name='order_info'),

]