# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from todo.models import ListItem

def home(request):
	items = ListItem.objects.filter(is_visible=True)
	return render_to_response('home.html', {'items': items}, context_instance = RequestContext(request))

def delete(request):
	if request.method == 'POST' and request.POST['id'] is not None:
		item = ListItem.objects.get(id=request.POST['id'])
		item.is_visible = False
		item.save()
	return render_to_response('home.html', {'items': ListItem.objects.filter(is_visible=True)}, context_instance = RequestContext(request))

def add(request):
	if request.method == 'POST' and request.POST['text'] is not None:
		ListItem.objects.create(text=request.POST['text'], is_visible=True)
	return render_to_response('home.html', {'items': ListItem.objects.filter(is_visible=True)}, context_instance = RequestContext(request))