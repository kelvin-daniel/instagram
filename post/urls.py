from django.urls import path
from post.views import index,NewPost
from . import views

urlpatterns = [
   	path('', views.index, name='index'),
	path('newpost/', NewPost, name='newpost'),
] 