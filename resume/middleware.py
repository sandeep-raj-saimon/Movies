#from django.conf  import settings
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class BookMiddleware(MiddlewareMixin):
	def __init__(self, get_response):
		self.get_response = get_response
		
	def process_request(self, request):
		print("Middleware executed")
		print(request.user.username)
		#return HttpResponse("some response")