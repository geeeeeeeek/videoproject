"""  URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from video import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('video/',include('video.urls')),
    path('myadmin/', include('myadmin.urls')),
    path('users/',include('users.urls')),
    path('comment/',include('comment.urls')),
    path('', views.IndexView.as_view(), name='home'), # 默认首页

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)