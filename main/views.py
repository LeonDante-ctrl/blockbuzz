from django.shortcuts import render
from .models import News

def home(request):
    first_news=News.objects.first()
    three_news=News.objects.all()[1:3]
    
    return render(request,'home.html', {
        'first_news':first_news,
        'three_news':three_news
    })
# Create your views here.
