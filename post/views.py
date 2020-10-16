from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from post.models import Post, Stream
from django.http import HttpResponse,Http404

# Create your views here.
@login_required
def index(request):
        user = request.user
        #gets all string objects created for user
        posts = Stream.objects.filter(user=user)

        #dict for posts
        group_ids = []
        for post in posts:
            group_ids.append(post.post_id)
        #filters all ids and order by -post for display in index
        post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')		
        
        return render(request, 'index.html',{'post_items': post_items})