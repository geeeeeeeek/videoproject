from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('subscribe/<int:pk>/', views.SubscribeView.as_view(), name='subscribe'),
    path('feedback/', views.FeedbackView.as_view(), name='feedback'),
    path('<int:pk>/collect_videos/', views.CollectListView.as_view(), name='collect_videos'),
    path('<int:pk>/like_videos/', views.LikeListView.as_view(), name='like_videos'),
]
