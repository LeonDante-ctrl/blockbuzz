from django.shortcuts import render
from .models import Category, News

def home(request):
    first_news=News.objects.first()
    three_news=News.objects.all()[1:3]
    three_categories=Category.objects.all()[0:3]
    
    return render(request,'home.html', {
        'first_news':first_news,
        'three_news':three_news,
        'three_categories':three_categories,
    })
    
def all_news(request):
    all_news=News.objects.all()
    return render(request,'all-news.html', {
        'all_news':all_news
    })    
# Create your views here.
