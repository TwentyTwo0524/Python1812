from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.index),

    url(r'^basedemo/$', views.basedemo),
    url(r'^includedemo/$', views.includedemo),
    url(r'^home/$', views.home),
    url(r'^cart/$', views.cart),
    url(r'^mine/$', views.mine),
]