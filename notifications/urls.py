from django.urls import path
from notifications.views import ShowNotifications

urlpatterns = [
   	path('', ShowNotifications, name='show-notifications'),

]