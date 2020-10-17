from django.urls import path
from post.views import index,NewPost, PostDetails
from . import views

urlpatterns = [
   	path('', views.index, name='index'),
	path('newpost/', NewPost, name='newpost'),
	path('<uuid:post_id>', PostDetails, name='postdetails'),
] 