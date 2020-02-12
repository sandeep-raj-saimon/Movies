# pages/urls.py
from django.urls import path
from .views import HomePageView,AboutPageView,LoginPageView,RegisterPageView
from django.contrib.auth import views as auth_views

urlpatterns = [
path('about/', AboutPageView.as_view(), name='about'), # new
path('login/', LoginPageView.as_view(), name='login'),
path('regsiter/', RegisterPageView.as_view(), name='register'), # new
#path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
path('', HomePageView.as_view(), name='home'),

]
