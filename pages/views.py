# pages/views.py
from django.views.generic import TemplateView
from django.urls import path, include,reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from pages.forms import UserForm,MoviesForm
from pages.models import *
#from django.core.urlresolvers import reverse

"""class HomePageView(TemplateView):
	template_name = 'home.html'"""
flag = False
person = None

class HomePageView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET': 
  
        # getting all the objects of hotel. 
            Movies_images = Movies_poster.objects.all()
            return render(request, "home.html",{'movies_images' : Movies_images,'flag':flag,'person':person})
            #return render(request,'home.html')
		
class AboutPageView(TemplateView):
	def get(self, request, *args, **kwargs):
	
		names = {"myname":"sandeep"}
		return render(request, "about.html",names)

class LoginPageView(TemplateView):
	def get(self, request, *args, **kwargs):
		print(args,kwargs)
		return render(request,"login.html")
	
	#new
	def post(self,request,*args,**kwargs):
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			
			user = authenticate(username=username, password=password)
			if user:
				if user.is_active:
					global flag
					global person
					
					flag=True
					person = username
					login(request,user)
					
					if username=="sandy" and password=="Sandeep@1997":
						url=reverse('upload')
						return HttpResponseRedirect(url)						
					else:
						url = reverse('home')
						#url = reverse('home',{'user': username,'flag':flag})
						#print(username,flag)
						return HttpResponseRedirect(url)
					
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

class UploadPageView(TemplateView):
	def get(self,request,*args,**kwargs):
		movies_form = MoviesForm()
		return render(request,'upload.html',{'movies_form':movies_form})
		
	def post(self,request,*args,**kwargs):
		if request.method == 'POST': 
			form = MoviesForm(request.POST, request.FILES) 
	  
			if form.is_valid(): 
				form.save() 
				return HttpResponse('success') 
		else:
			form = HotelForm() 
			return render(request,'upload.html',{'form':form})
	
class VideoPageView(TemplateView):
	def get(self,request,*args,**kwargs):
		print(args,kwargs)
		movie_name = kwargs['movie_name']
		Movies_images = Movies_poster.objects.all().filter(name=movie_name)
		#print(Movies_images)
		
		
		if flag==True:
			return render(request, "video.html",{'movies_images' : Movies_images,'flag':flag,'person':person})
		else:
			"""message="Login to continue"
			#return HttpResponse('Login to continue')
			return render(request,"login.html")"""
			url = reverse('login')
			return HttpResponseRedirect(url)
			
@login_required
def special(request):
    return HttpResponse("You are logged in !")
	
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

