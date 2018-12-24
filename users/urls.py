from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('subscribe/<int:pk>/', views.SubscribeView.as_view(), name='subscribe'),
    path('feedback/', views.FeedbackView.as_view(), name='feedback'),
    path('collect_videos/<int:pk>/', views.CollectListView.as_view(), name='collect_videos'),
    path('like_videos/<int:pk>', views.LikeListView.as_view(), name='like_videos'),

]
