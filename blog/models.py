from django.conf import settings
from django.db import models
from django.utils import timezone # from A import B : 파일 A에서 B를 추가해줘.


class Post(models.Model): #모델 정의 > class : 객체, post : 모델 이름, models 는 장고 모델임을 의미.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
