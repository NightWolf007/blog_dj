from jsonapi.api import API
from jsonapi.resource import Resource
from django.conf import settings

api = API()

@api.register
class UserResource(Resource):
	class Meta:
		model = settings.AUTH_USER_MODEL
		fieldnames_exclude = 'password',

@api.register
class PostResource(Resource):
	class Meta:
		model = 'blogapp.post'

@api.register
class CommentResource(Resource):
	class Meta:
		model = 'blogapp.comment'

@api.register
class TagResource(Resource):
	class Meta:
		model = 'blogapp.tag'