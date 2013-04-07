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

from django.http import HttpResponse

# Create your views here.
home_page = None #can't use this to resolve url bc it isn't a function (it isn't callable)
def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title></html>')
