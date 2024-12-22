from django.test import TestCase


from django.test import Client
from django.urls import reverse

from video.models import Video


class TestVideo(TestCase):

    @classmethod
    def setUpTestData(cls):
        # 创建一个测试用的实例
        cls.video = Video.objects.create(title='Good Title', desc='Good Desc')

    def test_video_title(self):
        # 检查标题是否正确
        self.assertEqual(self.video.title, 'Good Title')

