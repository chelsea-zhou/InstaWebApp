from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# hello world is a template view, inherit the template view
# there will be predefined method
class HelloWorld(TemplateView):
	# this is a field in this class, once we assigned it, we are done, the link is done
	# get method will return template_name
	template_name = 'test.html'