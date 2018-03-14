from django.conf.urls import url
from HotPotWebsite import views


urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^about', views.about, name = 'about'),
    url(r'^message_board/$', views.message_board, name='message_board'),
    url(r'^book/$', views.book, name='book'),
    url(r'^menu/$', views.menu, name='menu'),
]