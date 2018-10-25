from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/$', views.user_register, name='user_register'),
    url(r'^send_message/$', views.send_message, name='send_message'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^user_info/$', views.user_info, name='user_info'),
    url(r'^add_address/$', views.add_address, name='add_address'),
    url(r'^delete_address(?P<addr_id>\d+)/$', views.delete_address, name='delete_address'),
    url(r'^address_list/$', views.address_list, name='address_list'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
]