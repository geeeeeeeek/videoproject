import os

from chunked_upload.views import ChunkedUploadView, ChunkedUploadCompleteView
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import *
from django.views import generic
from django.views.generic import TemplateView

from comment.models import Comment
from helpers import get_page_data, SuperUserRequiredMixin, ajax_required
from video.models import Video
from .forms import UserLoginForm, VideoPublishForm, VideoEditForm
from .models import MyChunkedUpload


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None and user.is_superuser:
                auth_login(request, user)
                return redirect('myadmin:index')
            else:
                form.add_error('','请输入管理员账号')
    else:
        form = UserLoginForm()
    return render(request, 'myadmin/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('myadmin:login')


class IndexView(SuperUserRequiredMixin, generic.View):
    def get(self, request):
        return render(self.request, 'myadmin/index.html')


class AddVideoView(SuperUserRequiredMixin, TemplateView):
    template_name = 'myadmin/video_add.html'

class MyChunkedUploadView(ChunkedUploadView):

    model = MyChunkedUpload
    field_name = 'the_file'

class MyChunkedUploadCompleteView(ChunkedUploadCompleteView):

    model = MyChunkedUpload

    def on_completion(self, uploaded_file, request):

        print('uploaded--->', uploaded_file.size)
        print('uploaded--->', uploaded_file.name)
        pass

    def get_response_data(self, chunked_upload, request):
        video = Video.objects.create(file=chunked_upload.file)
        return {'code':0, 'video_id': video.id, 'msg':'success'}


class VideoPublishView(SuperUserRequiredMixin, generic.UpdateView):
    model = Video
    form_class = VideoPublishForm
    template_name = 'myadmin/video_publish.html'

    def get_success_url(self):
        return reverse('myadmin:video_publish_success')


class VideoPublishSuccessView(generic.TemplateView):
    template_name = 'myadmin/video_publish_success.html'


class VideoEditView(SuperUserRequiredMixin, generic.UpdateView):
    model = Video
    form_class = VideoEditForm
    template_name = 'myadmin/video_edit.html'

    def get_success_url(self):
        messages.success(self.request, "保存成功")
        return reverse('myadmin:video_edit', kwargs={'pk': self.kwargs['pk']})


@ajax_required
def video_delete(request):
    if not request.user.is_superuser:
        return JsonResponse({"code": 1, "msg": "请登录管理员账号"})
    video_id = request.POST['video_id']
    instance = Video.objects.get(id=video_id)
    instance.delete()
    return JsonResponse({"code": 0, "msg":"success"})


class VideoListView(SuperUserRequiredMixin, generic.ListView):
    model = Video
    template_name = 'myadmin/video_list.html'
    context_object_name = 'video_list'
    paginate_by = 10
    q = ''

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VideoListView, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        page_data = get_page_data(paginator, page)
        q_data = {'q': self.q}
        context.update(page_data)
        context.update(q_data)
        return context

    def get_queryset(self):
        self.q = self.request.GET.get("q", "")
        return Video.objects.filter(Q(title__contains=self.q)).order_by('-create_time')


class CommentListView(SuperUserRequiredMixin, generic.ListView):
    model = Comment
    template_name = 'myadmin/comment_list.html'
    context_object_name = 'comment_list'
    paginate_by = 10
    q = ''

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CommentListView, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        page_data = get_page_data(paginator, page)
        q_data = {'q': self.q}
        context.update(page_data)
        context.update(q_data)
        return context

    def get_queryset(self):
        self.q = self.request.GET.get("q", "")
        return Comment.objects.filter(Q(content__contains=self.q)).order_by('-timestamp')



@ajax_required
def comment_delete(request):
    if not request.user.is_superuser:
        return JsonResponse({"code": 1, "msg": "请登录管理员账号"})
    comment_id = request.POST['comment_id']
    instance = Comment.objects.get(id=comment_id)
    instance.delete()
    return JsonResponse({"code": 0, "msg":"success"})
