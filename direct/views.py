from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest

from django.contrib.auth.decorators import login_required

from direct.models import Message

# Create your views here.

@login_required
@login_required
def Inbox(request):
	messages = Message.get_messages(user=request.user)
	active_direct = None
	directs = None

	if messages:
		message = messages[0]
		active_direct = message['user'].username
		directs = Message.objects.filter(user=request.user, recipient=message['user'])
		directs.update(is_read=True)
		for message in messages:
			if message['user'].username == active_direct:
				message['unread'] = 0

	context = {
		'directs': directs,
		'messages': messages,
		'active_direct': active_direct,
		}

	template = loader.get_template('direct/direct.html')

	return HttpResponse(template.render(context, request))

