from django.urls import path
from . import views

app_name = 'video'
urlpatterns = [
    path('index', views.IndexView.as_view(), name='index'),
    path('search/', views.SearchListView.as_view(), name='search'),
    path('detail/<int:pk>/', views.VideoDetailView.as_view(), name='detail'),
    path('like/', views.like, name='like'),
    path('collect/', views.collect, name='collect'),
]