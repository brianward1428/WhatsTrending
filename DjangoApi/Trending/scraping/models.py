from django.db import models

# Create your models here.
class ProductHuntElement(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	upvotes = models.IntegerField()
	link =  models.URLField(max_length=600, null = True)

	def __str__ (self):
		return self.name

class GoogleSearchElement(models.Model):
	title = models.CharField(max_length=200)
	searchCount = models.CharField(max_length=500)
	link =  models.URLField(max_length=600, null = True)

	def __str__ (self):
		return self.title

class YouTubeElement(models.Model):
	title = models.CharField(max_length=200)
	info = models.CharField(max_length=500)
	link =  models.URLField(max_length=600, null = True)


	def __str__ (self):
		return self.title

class RedditActivityElement(models.Model):
	title = models.CharField(max_length=200)
	subscribers = models.CharField(max_length=100)
	link =  models.URLField(max_length=600, null = True)

	def __str__ (self):
		return self.title

class RedditGrowthElement(models.Model):
	title = models.CharField(max_length=200)
	growth = models.CharField(max_length=100)
	link =  models.URLField(max_length=600, null = True)

	def __str__ (self):
		return self.title

class RedditSubscribersElement(models.Model):
	title = models.CharField(max_length=200)
	subscribers = models.CharField(max_length=100)
	link =  models.URLField(max_length=600, null = True)

	def __str__ (self):
		return self.title
