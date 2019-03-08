from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.home, name='home'),  # 首页

    # url(r'^market/$', views.market, name='marketbase'), # 闪购超市
    # url(r'^market/(\d+)/$', views.market, name='market'), # 闪购超市
    url(r'^market/$', views.market, name='market'),

    url(r'^cart/$', views.cart, name='cart'),   # 购物车
    url(r'^mine/$', views.mine, name='mine'),   # 我的
]