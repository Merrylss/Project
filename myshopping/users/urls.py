from django.conf.urls import url

from . import views

# app_name = 'users'

urlpatterns = [
    url(r'^user_register/$', views.user_register, name='user_register'),
    url(r'^user_login/$', views.user_login, name='user_login')
]