from django.urls import path
from direct.views import Inbox, Directs, SendDirect, UserSearch

urlpatterns = [
   	path('', Inbox, name='inbox'),
    path('directs/<username>', Directs, name='directs'),
    path('new/', UserSearch, name='usersearch'),
    path('send/', SendDirect, name='send_direct'),
]