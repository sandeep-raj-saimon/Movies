from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.user.username

class Movies_poster(models.Model): 
    name = models.CharField(max_length=50) 
    movie_Img = models.ImageField(upload_to='images/')
	