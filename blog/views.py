from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts= [

    {
        'author': "Kailyn Williams",
        'title': "The Big Man!",
        'post_num': "1",
        'post_type': "basketball",
        'date': 'August 19, 2019'
    },

     {
        'author': "Kelsea Williams",
        'title': "The Little Girl",
        'post_num': "2",
        'post_type': "soccer",
        'date': 'January 1st, 2019'
    }
]

def home(request):
    context={
        'posts': posts
    }
    return render( request, "blog/home.html", context)


def about(request):
    return render(request, 'blog/about.html', {'title': "Django-Blog: About"})

