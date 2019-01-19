from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

authorlist = [
     {'author':'Ram','date_posted':'5 feb','title':'Sky', 'content':'Sky is blue and sky has no limit'},
     {'author':'Hasan','date_posted':'7 feb','title':'water', 'content':'Water has no color'}]

def home(request):

    context={
        'posts':authorlist
    }
    return render(request,'blog/home.html', context)


def about(request):
    return render(request,'blog/about.html', {'title':'About'})