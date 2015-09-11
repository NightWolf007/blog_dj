from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Post(models.Model):
	user = models.ForeignKey(User)
	tags = models.ManyToManyField(Tag)

	title = models.CharField(max_length=255)
	text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


class Comment(models.Model):
	user = models.ForeignKey(User)
	post = models.ForeignKey(Post)

	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.message

# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
# 	if created:
# 		Token.objects.create(user=instance)