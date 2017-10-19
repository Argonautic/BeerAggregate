from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns =  [
    url(r'^$', views.api_root),
    url(r'^users/$', views.UserList.as_view(), name="user-list"),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name="user-detail"),
    url(r'^breweries/$', views.BreweryList.as_view(), name="brewery-list"),
    url(r'^breweries/(?P<pk>[0-9]+)/$', views.BreweryDetail.as_view(), name="brewery-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]