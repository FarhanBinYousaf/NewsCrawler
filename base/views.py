from django.shortcuts import render
from .models import News
# Create your views here.

def home(request):
    latest = News.objects.all()
    context = {'latest':latest}
    return render(request,'base/latestNews.html',context)
