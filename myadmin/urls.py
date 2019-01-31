from django.urls import path
from . import views

app_name = 'myadmin'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    #----------------------总览---------------------------
    path('', views.IndexView.as_view(), name='index'),

    #----------------------视频管理------------------------
    path('video_list/', views.VideoListView.as_view(), name='video_list'),
    path('video_add/', views.AddVideoView.as_view(), name='video_add'),

    path('chunked_upload/',  views.MyChunkedUploadView.as_view(), name='api_chunked_upload'),
    path('chunked_upload_complete/', views.MyChunkedUploadCompleteView.as_view(),name='api_chunked_upload_complete'),

    path('video_publish/<int:pk>/', views.VideoPublishView.as_view(), name='video_publish'),
    path('video_publish_success/', views.VideoPublishSuccessView.as_view(), name='video_publish_success'),
    path('video_edit/<int:pk>/', views.VideoEditView.as_view(), name='video_edit'),
    path('video_delete/', views.video_delete, name='video_delete'),

    #----------------------分类管理----------------------------
    path('classification_add/', views.ClassificationAddView.as_view(), name='classification_add'),
    path('classification_list/', views.ClassificationListView.as_view(), name='classification_list'),
    path('classification_edit/<int:pk>/', views.ClassificationEditView.as_view(), name='classification_edit'),
    path('classification_delete/', views.classification_delete, name='classification_delete'),

    #----------------------评论管理----------------------------
    path('comment_list/', views.CommentListView.as_view(), name='comment_list'),
    path('comment_delete/', views.comment_delete, name='comment_delete'),

    #----------------------用户管理-------------------------
    path('user_add/', views.UserAddView.as_view(), name='user_add'),
    path('user_list/', views.UserListView.as_view(), name='user_list'),
    path('user_edit/<int:pk>',views.UserEditView.as_view(), name='user_edit'),
    path('user_delete/', views.user_delete, name='user_delete'),

    #-----------------------订阅通知-------------------------
    path('subscribe/', views.SubscribeView.as_view(), name='subscribe'),

    # -----------------------用户反馈-------------------------
    path('feedback_list/', views.FeedbackListView.as_view(), name='feedback_list'),
    path('feedback_delete/', views.feedback_delete, name='feedback_delete'),
]