from django.conf import settings
from django.db import models


class TimeStampedMixin(models.Model):
    # 생성일시, 수정일시를 저장한다
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Postable(TimeStampedMixin):
    # 자동으로 생성일시, 수정일시 필드가 추가된다
    # 작성자와 내용을 저장한다
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='작성자')
    content = models.CharField(max_length=100, verbose_name='내용')

    class Meta:
        abstract=True
