from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import *
from django.views import generic
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mass_mail
import smtplib
from helpers import get_page_data, ajax_required
from .forms import CommentForm
from .models import Video


@login_required(login_url='/users/login')
def add_video(request):
    Video.objects.create(title='java', desc='我是java哈哈哈')
    return HttpResponse("success")

# todo write for future
def send_email(request):
    try:
        to_list = ['net19880504@126.com','net936@163.com','912750350@qq.com']
        message = ('测试主题', '你好hello', 'net936@163.com', to_list)
        # do not forget set password
        send_mass_mail((message,))
    except smtplib.SMTPException :
        print("--> send fail")
        return HttpResponse("fail")
    else:
        print("--> send success")
        return HttpResponse("success")


class IndexView(generic.ListView):
    model = Video
    template_name = 'video/index.html'
    context_object_name = 'video_list'
    paginate_by = 4
    ordering = ['-create_time']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        page_data = get_page_data(paginator, page)
        context.update(page_data)
        return context


class SearchListView(generic.ListView):
    model = Video
    template_name = 'video/search_result.html'
    context_object_name = 'video_list'
    paginate_by = 4
    q = ''

    def get_queryset(self):
        self.q = self.request.GET.get("q","")
        return Video.objects.filter(Q(title__contains=self.q))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchListView, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        page_data = get_page_data(paginator, page)
        q_data = {'q': self.q}
        context.update(page_data)
        context.update(q_data)
        return context


class VideoDetailView(generic.DetailView):
    model = Video
    template_name = 'video/detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.view_count += 1
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super(VideoDetailView, self).get_context_data(**kwargs)
        # 推荐数据
        recommend_list = Video.objects.order_by('-view_count')[:4]
        recommend_data = {'recommend_list':recommend_list}

        form = CommentForm()
        form_data = {'form':form}
        context.update(recommend_data)
        context.update(form_data)
        return context

@ajax_required
@require_http_methods(["POST"])
def like(request):
    if not request.user.is_authenticated:
        return JsonResponse({"code": 1, "msg": "请先登录"})
    video_id = request.POST['video_id']
    video = Video.objects.get(pk=video_id)
    user = request.user
    video.switch_like(user)
    return JsonResponse({"code": 0, "likes": video.count_likers(), "user_liked": video.user_liked(user)})


@ajax_required
@require_http_methods(["POST"])
def collect(request):
    if not request.user.is_authenticated:
        return JsonResponse({"code": 1, "msg": "请先登录"})
    video_id = request.POST['video_id']
    video = Video.objects.get(pk=video_id)
    user = request.user
    video.switch_collect(user)
    return JsonResponse({"code": 0, "collects": video.count_collecters(), "user_collected": video.user_collected(user)})



