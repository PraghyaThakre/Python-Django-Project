from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<em>My Second app</em>')  #<em></em> is a html syntax for italic type pattern of character

def help(request):
    help_dict = {'help_me':'Welcome to my help page'}
    return render(request,'help_page/help.html',context=help_dict)
# Create your views here.
