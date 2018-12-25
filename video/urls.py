from django.urls import path
from . import views

app_name = 'video'
urlpatterns = [
    path('index', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', views.VideoDetailView.as_view(), name='detail'),
    path('search_result/', views.SearchListView.as_view(), name='search_result'),
    path('like/', views.like, name='like'),
    path('collect/', views.collect, name='collect'),
]