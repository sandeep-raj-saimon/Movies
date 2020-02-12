# pages/views.py
from django.views.generic import TemplateView
from django.urls import path, include,reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from pages.forms import UserForm

"""class HomePageView(TemplateView):
	template_name = 'home.html'"""

class HomePageView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "home.html")
		
class AboutPageView(TemplateView):
	def get(self, request, *args, **kwargs):
	
		names = {"myname":"sandeep"}
		return render(request, "about.html",names)

class LoginPageView(TemplateView):
	def get(self, request, *args, **kwargs):
		return render(request,"login.html")
	
	#new
	def post(self,request,*args,**kwargs):
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(username=username, password=password)
			if user:
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect(reverse('home'))
				else:
					return HttpResponse("Your account was inactive.")
			else:
				print("Someone tried to login and failed.")
				print("They used username: {} and password: {}".format(username,password))
				return HttpResponse("Invalid login details given")
		else:
			return render(request, 'login.html', {})
			
			
class RegisterPageView(TemplateView):
	
	#new
	def get(self, request, *args, **kwargs):
		registered=False
		user_form = UserForm()
		
		return render(request,'register.html',{'user_form':user_form,'registered':registered})
	
		
	def post(self,request,*args,**kwargs):
		registered = False
		if request.method == 'POST':
			user_form = UserForm(data=request.POST)
			
			if user_form.is_valid():
				user = user_form.save()
				user.set_password(user.password)
				user.save()
				registered = True
			else:
				print(user_form.errors)
		else:
			user_form = UserForm()
		
		return render(request,'register.html',{'user_form':user_form,'registered':registered})

#new

@login_required
def special(request):
    return HttpResponse("You are logged in !")
	
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

