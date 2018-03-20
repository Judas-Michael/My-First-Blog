from django.db import models

from django.utils import timezone

class Post(models.Model): 

#creates class for posting information 
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank = True, null = True)
		
	#establishes each part of a post and what's allowed inside those parts
		
	def publish(self): 
	
	#method for publishing post and assigning time
		self.published_date =timezone.now
		self.save()
	
	def __str__(self):
	
	#reminding the code that it is referring to itself in the present
		return self.title