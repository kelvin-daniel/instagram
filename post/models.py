from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils.text import slugify
import uuid

# Create your models here.

#upload file to media_root /user_id/filename
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Tag(models.Model):
	title = models.CharField(max_length=60, verbose_name='Tag')
	slug = models.SlugField(null=False, unique=True)

	class Meta:
		verbose_name='Tag'
		verbose_name_plural = 'Tags'

# when clicked creates url with slug
	def get_absolute_url(self):
		return reverse('tags', args=[self.slug])
		
	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		return super().save(*args, **kwargs)
    
class Post(models.Model):
    #creates random id for posts
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	picture =  models.ImageField(upload_to=user_directory_path, verbose_name='Picture', null=False)
	caption = models.TextField(max_length=1500, verbose_name='Caption')
	posted = models.DateTimeField(auto_now_add=True)
	tags = models.ManyToManyField(Tag, related_name='tags')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	likes = models.IntegerField(default=0)


	def get_absolute_url(self):
		return reverse('postdetails', args=[str(self.id)])

	def __str__(self):
		return str(self.id)

class Follow(models.Model):
	follower = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='follower')
	following = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='following')

	def user_follow(sender, instance, *args, **kwargs):
		follow = instance
		sender = follow.follower
		following = follow.following
		notify = Notification(sender=sender, user=following, notification_type=3)
		notify.save()

	def user_unfollow(sender, instance, *args, **kwargs):
		follow = instance
		sender = follow.follower
		following = follow.following

		notify = Notification.objects.filter(sender=sender, user=following, notification_type=3)
		notify.delete()

#sends new posts to users following you
class Stream(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='stream_following')
    user = models.ForeignKey(User, on_delete=models.CASCADE)   
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField()

    def add_post(sender, instance, *args, **kwargs):
    	post = instance
    	user = post.user
        #filter followers following you
    	followers = Follow.objects.all().filter(following=user)
        #loop to stream to your followers
    	for follower in followers:
    		stream = Stream(post=post, user=follower.follower, date=post.posted, following=user)
    		stream.save()

#streams everytime a post is made
post_save.connect(Stream.add_post, sender=Post)