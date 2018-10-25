from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^store_add/$', views.store_add, name='store_add'),
    url(r'^store_list/', views.store_list, name='store_list'),
    url(r'^(?P<s_id>\d+)/store_info/', views.store_info, name='store_info'),
    url(r'^(?P<store_id>\d+)/store_update/', views.store_update, name='store_update'),
    url(r'^(?P<store_id>\d+)/store_close/', views.store_close, name='store_close'),
    url(r'^(?P<store_id>\d+)/store_del/', views.store_del, name='store_del'),
    url(r'^store_update/', views.store_update, name='store_update'),
]