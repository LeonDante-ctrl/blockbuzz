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

def detail(request,id):
    news=News.objects.get(pk=id)
    category=Category.objects.get(id=news.category.id)
    sim_news=News.objects.filter(category=category).exclude(id=id)
    return render(request,'detail.html',{
        'news':news,
        'similar_news':sim_news
    })
    
    
#cfetching all category
def all_category(request):
    cats=Category.objects.all()
    return render(request,'category.html',{
        'cats':cats
    })   
    
def category(request,id):
    category=Category.objects.get(id=id)
    news=News.objects.filter(category=category)
    return render(request,'category-news.html',{
        'all_news':news,
        'category':category
    })