from django.shortcuts import render
from .models import Feed, Comment

# Create your views here.
def index(request):
    feeds = Feed.objects.all()
    context = {
        'feeds':feeds,
    }
    return render(request,'feeds/index.html',context)