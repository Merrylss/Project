from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<store_id>\d+)/goods_upload/$', views.goods_upload, name='goods_upload'),
    url(r'^(?P<goods_id>\d+)/goods_info/$', views.goods_info, name='goods_info'),
    url(r'^goodstype/$', views.goodstype, name='goodstype'),
    url(r'^man_goods/$', views.man_goods, name='man_goods'),
    url(r'^women_goods/$', views.women_goods, name='women_goods'),
    url(r'^children_goods/$', views.children_goods, name='children_goods'),
]