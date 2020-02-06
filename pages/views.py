# pages/views.py
from django.views.generic import TemplateView
from django.urls import path, include
from django.shortcuts import render
from django.http import HttpResponse

 
"""class HomePageView(TemplateView):
	template_name = 'home.html'"""

class HomePageView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "home.html")
		
class AboutPageView(TemplateView):
	def get(self, request, *args, **kwargs):
	
		names = {"myname":"sandeep"}
		return render(request, "about.html",names)

"""class LoginPageView(TemplateView):
	template_name='login.html'""" 
	
