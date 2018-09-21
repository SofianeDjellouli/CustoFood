from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from main import views

urlpatterns = [
	url(r'', admin.site.urls),
    url(r'^options/$', views.OptionsList.as_view()),
    url(r'^options/(?P<pk>[0-9]+)/$', views.OptionDetail.as_view()),
    url(r'^products/$', views.ProductsList.as_view()),
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    url(r'^categories/$', views.CategoriesList.as_view()),
    url(r'^categories/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
    url(r'^choice/$', views.ChoiceList.as_view()),
    url(r'^choice/(?P<pk>[0-9]+)/$', views.ChoiceDetail.as_view()),
    url(r'^cart/$', views.CartList.as_view()),
    url(r'^cart/(?P<pk>[0-9]+)/$', views.CartDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)