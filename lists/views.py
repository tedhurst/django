from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def home_page(request):
#    return HttpResponse('<html><title>To-Do lists</title></html>')
def home_page(request):
    return render(request, 'home.html')

#home_page = None
