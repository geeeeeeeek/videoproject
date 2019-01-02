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
    if request.method == 'POST':
        next = request.POST.get('next', '/')
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                # return redirect('home')
                return redirect(next)
        else:
            print(form.errors)
    else:
        next = request.GET.get('next', '/')
        form = UserLoginForm()
    print(next)
    return render(request, 'registration/login.html', {'form': form, 'next':next})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password1)
            auth_login(request, user)
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('home')


def change_password(request):
    if request.method == 'POST':
        form = ChangePwdForm(request.user, request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if not user.is_staff and not user.is_superuser:
                user.save()
                update_session_auth_hash(request, user)  # 更新session 非常重要！
                messages.success(request, '修改成功')
                return redirect('users:change_password')
            else:
                messages.warning(request, '无权修改管理员密码')
                return redirect('users:change_password')
        else:
            print(form.errors)
    else:
        form = ChangePwdForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })


class ProfileView(LoginRequiredMixin,AuthorRequiredMixin, generic.UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'users/profile.html'

    def get_success_url(self):
        messages.success(self.request, "保存成功")
        return reverse('users:profile', kwargs={'pk': self.request.user.pk})


class SubscribeView(LoginRequiredMixin,AuthorRequiredMixin, generic.UpdateView):
    model = User
    form_class = SubscribeForm
    template_name = 'users/subscribe.html'

    def get_success_url(self):
        messages.success(self.request, "保存成功")
        return reverse('users:subscribe', kwargs={'pk': self.request.user.pk})

class FeedbackView(LoginRequiredMixin, generic.CreateView):

    model = Feedback
    form_class = FeedbackForm
    template_name = 'users/feedback.html'

    @ratelimit(key='ip', rate='2/m')
    def post(self, request, *args, **kwargs):
        was_limited = getattr(request, 'limited', False)
        if was_limited:
            messages.warning(self.request, "操作太频繁了，请1分钟后再试")
            return render(request, 'users/feedback.html', {'form': FeedbackForm()})
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, "提交成功")
        return reverse('users:feedback')

class CollectListView(generic.ListView):
    model = User
    template_name = 'users/collect_videos.html'
    context_object_name = 'video_list'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CollectListView, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        page_list = get_page_list(paginator, page)
        context['page_list'] = page_list
        return context
    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        videos = user.collected_videos.all()
        return videos


class LikeListView(generic.ListView):
    model = User
    template_name = 'users/like_videos.html'
    context_object_name = 'video_list'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LikeListView, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        page_list = get_page_list(paginator, page)
        context['page_list'] = page_list
        return context

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        videos = user.liked_videos.all()
        return videos