# pages/urls.py
from django.urls import path,re_path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
path('about/', AboutPageView.as_view(), name='about'), # new
path('login/', LoginPageView.as_view(), name='login'),
path('logout/',LogoutPageView.as_view(), name = 'logout'),
path('regsiter/', RegisterPageView.as_view(), name='register'), # new
path('upload/',UploadPageView.as_view(),name='upload'),
path(r'^video/(?P<movie_name>\d+)/$', VideoPageView.as_view(), name='video'),
path('search/', SearchPageView.as_view(), name='search'),
#path(r'^search/(?P<movie_name>\d+)/$', SearchPageView.as_view(), name='search'),
#path('video/',VideoPageView.as_view(),name='video'),
#path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
path('', HomePageView.as_view(), name='home'),
#path('setcookie', setcookie),
#path('getcookie', showcookie),
path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',activate, name='activate'),
]
