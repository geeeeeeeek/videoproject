from helpers import AuthorRequiredMixin, get_page_list
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import *
from django.views import generic
from ratelimit.decorators import ratelimit

from .models import Feedback

from .forms import ProfileForm, SignUpForm, UserLoginForm, ChangePwdForm, SubscribeForm, FeedbackForm

User = get_user_model()


def login(request):
    # 功能待开发，请期待

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        videos = user.liked_videos.all()
        return videos
