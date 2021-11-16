from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): 
	return render(request, "index.html", {})

def about_view(request, *args, **kwargs): 
	my_context={
		"my_text": "this is my text",
		"my_number": 123,
		"my_list": {"Ram", "Hari", "Rajan"}
	}
	return render(request, "about.html", my_context)

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})