from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from main import views

urlpatterns = [
    url(r'^options/$', views.OptionsList.as_view()),
	url(r'^products/$', views.ProductsList.as_view()),
	url(r'^categories/$', views.CategoriesList.as_view()),
	url(r'^choice/$', views.ChoiceList.as_view()),
	url(r'^cart/$', views.CartList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)