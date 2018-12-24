from django.urls import path

from . import views

app_name = 'myadmin'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('video_list/', views.VideoListView.as_view(), name='video_list'),
    path('video_add/', views.AddVideoView.as_view(), name='video_add'),

    path('chunked_upload/',  views.MyChunkedUploadView.as_view(), name='api_chunked_upload'),
    path('chunked_upload_complete/', views.MyChunkedUploadCompleteView.as_view(),name='api_chunked_upload_complete'),

    path('video_publish/<int:pk>/', views.VideoPublishView.as_view(), name='video_publish'),
    path('video_publish_success/', views.VideoPublishSuccessView.as_view(), name='video_publish_success'),
    path('video_edit/<int:pk>/', views.VideoEditView.as_view(), name='video_edit'),
    path('video_delete/', views.video_delete, name='video_delete'),

    #----------------------评论url-------------------------
    path('comment_list/', views.CommentListView.as_view(), name='comment_list'),
    path('commend_delete', views.comment_delete, name='comment_delete'),
]