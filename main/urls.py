from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home,name='home'),
    path('all_news', views.all_news,name='all_news'),
    path('detail/<int:id>', views.detail,name='detail'),
    path('all-category', views.all_category,name='all-category'),
     path('category/<int:id>',views.category,name='category'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
