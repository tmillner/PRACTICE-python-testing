####################ALL VERSIONS OF WRITING DO THE SAME THING##################333
##import django
##
### Create your views here.
##home_page = None #can't use this to resolve url bc it isn't a function (it isn't callable)
##def home_page(request):
##    return django.http.HttpResponse()

##import django.http
##
### Create your views here.
##home_page = None #can't use this to resolve url bc it isn't a function (it isn't callable)
##def home_page(request):
##    return django.http.HttpResponse()

##from django.http import HttpResponse
##
### Create your views here.
##home_page = None #can't use this to resolve url bc it isn't a function (it isn't callable)
##def home_page(request):
##    return HttpResonse('<html><title>To-Do list</title></html>')

from django.shortcuts import render

# Create your views here.
home_page = None #can't use this to resolve url bc it isn't a function (it isn't callable)
def home_page(request):
    return render(request, "home.html")
