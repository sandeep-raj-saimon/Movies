# pages/views.py
from django.views.generic import TemplateView
from django.urls import path, include,reverse
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from pages.forms import UserForm,MoviesForm
from pages.models import *
import datetime
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.db.models import Q
import threading
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

flag = False
person = None
message = None

class HomePageView(TemplateView):
    def get(self, request, *args, **kwargs):
        username = request.COOKIES['username']
        last_connection = request.COOKIES['last_connection']
        last_connection_time = datetime.datetime.strptime(last_connection[:-7],'%Y-%m-%d %H:%M:%S')
        print(last_connection_time-datetime.datetime.now())
		
        if (datetime.datetime.now() - last_connection_time).seconds < 10:
            pass
        else:
            #print("not logged in")
            global flag
            global person
			
            flag = False
            person = None
						
        if request.method == 'GET': 
		
        # getting all the objects of hotel. 
            #print(person,flag)
            Movies_images = Movies_poster.objects.all()
            return render(request, "home.html",{'movies_images' : Movies_images,'flag':flag,'person':person})
            
class AboutPageView(TemplateView):
	def get(self, request, *args, **kwargs):
	
		names = {"myname":"sandeep"}
		return render(request, "about.html",names)

class LoginPageView(TemplateView):
	def get(self, request, *args, **kwargs):
		#print(args,kwargs)
		if request.method == 'GET':
			
			"""users = User.objects.all()
			for user in users:
				print(len(user.username),":",len(user.password))"""
			
			if message is None:
				return render(request,"login.html")
			else:
				return render(request,"login.html",{'message':message})

			
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
								
					if username=="Sandeep@1997" and password=="Sandeep@1997":
						url=reverse('upload')
						response = HttpResponseRedirect(url)
						#return url
						#response = render_to_response(request,'about.html',{"username":username})
			
					else:
						url = reverse('home')
						response= HttpResponseRedirect(url)
						
						#response = render_to_response(request,'about.html',{"username":username})
					response.set_cookie('last_connection',datetime.datetime.now())
					response.set_cookie('username',datetime.datetime.now())
					
					return response
				else:
					return HttpResponse("Your account was inactive.")
			else:
				print("Someone tried to login and failed.")
				print("They used username: {} and password: {}".format(username,password))
				return HttpResponse("Invalid login details given")
		else:
			return render(request, 'login.html', {})
			
class LogoutPageView(TemplateView):
	def get(self,request,*args,**kwargs):
		try:
			del request.session['username']
			
			global flag
			global person
			
			flag = False
			person = None
			
		except:
			pass
			
		print(flag,person)
		return HttpResponse("<strong>You are logged out.</strong>")
		
class RegisterPageView(TemplateView):
	
	#new
	def get(self, request, *args, **kwargs):
		registered=False
		user_form = UserForm()
		
		return render(request,'register.html',{'user_form':user_form,'registered':registered})
	
		
	def post(self,request,*args,**kwargs):
		registered = False
		if request.method == 'POST':
			form = UserForm(data=request.POST)
			
			if form.is_valid():
				user = form.save()
				#user.is_active = False
				#print(user.password)
				#user.save()
							
				current_site = get_current_site(request)
				mail_subject = 'Activate your blog account.'
				message = render_to_string('acc_active_email.html', {
					'user': user,
					'domain': current_site.domain,
					'uid':urlsafe_base64_encode(force_bytes(user.pk)),
					'token':account_activation_token.make_token(user),
				})
				to_email = form.cleaned_data.get('email')
				email = EmailMessage(
							mail_subject, message, to=[to_email]
				)
				email.send()
				#registered = True
				#print("registered")
				return HttpResponse('Please confirm your email address to complete the registration')
			else:
				print(form.errors)
		else:
			user_form = UserForm()
		
		#return render(request,'register.html',{'user_form':user_form,'registered':registered})
		return render(request,'register.html',{'user_form':form})

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
		#print(args,kwargs)
		movie_name = kwargs['movie_name']
		Movies_images = Movies_poster.objects.all().filter(name=movie_name)
		
		if flag==True:
			return render(request, "video.html",{'movies_images' : Movies_images,'flag':flag,'person':person})
		else:
			global message
			message = "Login to continue"
			url = reverse('login')
			return HttpResponseRedirect(url)

class SearchPageView(TemplateView):
	def post(self,request,*args,**kwargs):
		if request.method=='POST':
			search = request.POST['search']
			
			if search:
				match = Movies_poster.objects.all().filter(Q(name__icontains=search))
				#print(match)
				if match:
					return render(request,"search.html",{"matches":match})
				else:
					return render(request,"base.html",{"no_movie":"No Movie Exists"})
			else:
				return render(request,"base.html",{"invalid_search":"invalid_search"})
				
#for activating the account
def activate(request, uidb64, token):
    uidb64 = str.encode(uidb64)[2:5]
    
    #print(idi==uidb64)
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        #print(uid,user)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and account_activation_token.check_token(user, token):
        #print("password",user.password,len(user.password))
        user.set_password(user.password)
        user.save()
        user.is_active = True
        #login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
		
"""		
#for cookies
def setcookie(request):
    html = HttpResponse("<h1>Dataflair Django Tutorial</h1>")
    if request.COOKIES.get('visits'):
        html.set_cookie('dataflair', 'Welcome Back')
        value = int(request.COOKIES.get('visits'))
        html.set_cookie('visits', value + 1)
    else:
        value = 1
        text = "Welcome for the first time"
        html.set_cookie('visits', value)
        html.set_cookie('dataflair', text)
    return html

def showcookie(request):
    if request.COOKIES.get('visits') is not None:
        value = request.COOKIES.get('visits')
        text = request.COOKIES.get('dataflair')
        html = HttpResponse("<center><h1>{0}<br>You have requested this page {1} times</h1></center>".format(text, value))
        html.set_cookie('visits', int(value) + 1)
        return html
    else:
        print("show cookie")
        return redirect('/setcookie')
"""