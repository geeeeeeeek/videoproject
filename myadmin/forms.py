from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User
from video.models import Video


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(min_length=4,max_length=30,
                               error_messages={
                                   'min_length': '用户名不少于4个字符',
                                   'max_length': '用户名不能多于30个字符',
                                   'required': '用户名不能为空',
                               },
                               widget=forms.TextInput(attrs={'placeholder': '请输入用户名'}))
    password = forms.CharField(min_length=8,max_length=30,
                               error_messages={
                                   'min_length': '密码不少于8个字符',
                                   'max_length': '密码不能多于30个字符',
                                   'required': '密码不能为空',
                               },
                               widget=forms.PasswordInput(attrs={'placeholder': '请输入密码'}))

    class Meta:
        model = User
        fields = ['username', 'password']

    error_messages = {'invalid_login': '用户名或密码错误', }


class VideoPublishForm(forms.ModelForm):
    title = forms.CharField(min_length=4, max_length=200, required=True,
                              error_messages={
                                  'min_length': '至少4个字符',
                                  'max_length': '不能多于200个字符',
                                  'required': '标题不能为空'
                              },
                              widget=forms.TextInput(attrs={'placeholder': '请输入内容'}))
    desc = forms.CharField(min_length=4, max_length=200, required=True,
                              error_messages={
                                  'min_length': '至少4个字符',
                                  'max_length': '不能多于200个字符',
                                  'required': '描述不能为空'
                              },
                              widget=forms.Textarea(attrs={'placeholder': '请输入内容'}))
    cover = forms.ImageField(required=True,
                             error_messages={
                                 'required': '封面不能为空'
                             },
                             widget=forms.FileInput(attrs={'class' : 'n'}))
    status = forms.CharField(min_length=1, max_length=1, required=False,
                             widget=forms.HiddenInput(attrs={'value':'0'}))
    class Meta:
        model = Video
        fields = ['title', 'desc','status', 'cover']


class VideoEditForm(forms.ModelForm):
    title = forms.CharField(min_length=4, max_length=200, required=True,
                              error_messages={
                                  'min_length': '至少4个字符',
                                  'max_length': '不能多于200个字符',
                                  'required': '标题不能为空'
                              },
                              widget=forms.TextInput(attrs={'placeholder': '请输入内容'}))
    desc = forms.CharField(min_length=4, max_length=200, required=True,
                              error_messages={
                                  'min_length': '至少4个字符',
                                  'max_length': '不能多于200个字符',
                                  'required': '描述不能为空'
                              },
                              widget=forms.Textarea(attrs={'placeholder': '请输入内容'}))
    cover = forms.ImageField(required=True,
                             error_messages={
                                 'required': '封面不能为空'
                             },
                             widget=forms.FileInput(attrs={'class' : 'n'}))

    status = forms.CharField(min_length=1,max_length=1,required=False,
                             widget=forms.HiddenInput())

    class Meta:
        model = Video
        fields = ['title', 'desc', 'status', 'cover']