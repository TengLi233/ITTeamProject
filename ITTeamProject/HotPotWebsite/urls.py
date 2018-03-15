from django.conf.urls import url
from HotPotWebsite import views


urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^about', views.about, name = 'about'),
    url(r'^message_board/$', views.message_board, name='message_board'),
    url(r'^book/$', views.book, name='book'),
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
]