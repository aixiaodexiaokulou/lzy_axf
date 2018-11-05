from django.conf.urls import url

from axf import views

urlpatterns = [
    url(r'^$', views.home, name='index'), # 首页
    url(r'^home/$', views.home, name='home'),# 首页
    url(r'^market/(\d+)/(\d+)/(\d+)/$', views.market, name='market'),  # 闪购超市
    url(r'^cart/$', views.cart, name='cart'),  # 闪购超市
    url(r'^mine/$', views.mine, name='mine'),  # 闪购超市
    url(r'^registe/$', views.registe, name='registe'),  # 注册

]