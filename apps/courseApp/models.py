from __future__ import unicode_literals

from django.db import models

class BlogManager(models.Manager):
	def basic_validations(self, postData):
		errors = {}
		if len(postData['course']) < 6:
			errors['name'] = "Please add correct name"
		if len(postData['desc']) < 16:
			errors['desc'] = "Please add more desc"
		return errors

class Course(models.Model):
	name = models.CharField(max_length=100)
	desc = models.CharField(max_length=150)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = BlogManager()

# Create your models here.
