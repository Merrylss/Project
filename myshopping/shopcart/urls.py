from django.conf.urls import url

from . import views

app_name = 'shopcart'

urlpatterns = [
    url(r'^(?P<goods_id>\d+)/(?P<count>\d+)/shop_cart_add/$', views.shop_cart_add, name='shop_cart_add'),
    url(r'^shop_cart_info/$', views.shop_cart_info, name='shop_cart_info'),
    url(r'^(?P<goods_id>\d+)/shop_cart_del/$', views.shop_cart_del, name='shop_cart_del'),
    url(r'^(?P<goods_id>\d+)/(?P<i>\d+)/shop_cart_update/$', views.shop_cart_update, name='shop_cart_update'),
]