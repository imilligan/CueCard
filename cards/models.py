import datetime

from django.db import models
from django.utils import timezone

class Author(models.Model):
	first = models.CharField(max_length=256)
	middle = models.CharField(max_length=256)
	last = models.CharField(max_length=256)

	def displayName(self):
		return str(self)

	def __str__(self):
		return self.first + " " + self.middle + " " + self.last

class Source(models.Model):
	author = models.ForeignKey(Author)
	# TODO: Make more general title class
	title = models.CharField(max_length=512)

	def __str__(self):
		return self.title

class Card(models.Model):
	info = models.TextField()
	code = models.CharField(max_length=256)
	citation = models.ForeignKey(Source)
	start_page = models.IntegerField(default=0)
	end_page = models.IntegerField(default=0)
	last_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		# TODO: A real string concat method
		return self.info[:16] + "..."

class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date < now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

	def __str__(self):
		return self.question

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text
