# from django.urls import path
# from news.views import scrape, news_list
# urlpatterns = [
#   path('scrape/<str:name>', scrape, name="scrape"),
#   path('', news_list, name="home"),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('scrape/<str:name>/', views.scrape, name="scrape"),
]
