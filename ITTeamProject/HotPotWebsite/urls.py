from django.conf.urls import url
from HotPotWebsite import views


urlpatterns = [
    url(r'^$', views.index, name = 'index'),
]