from django.conf import settings
from django.db import models


# 인스타그램 사진을 업로드하면 저장할 경로를 지정한다
from django.utils.timezone import now

from Instagram_clone.mixins import TimeStampedMixin, Postable


def get_instagram_photo_path(instance, filename):
    return 'media/feed/{:%Y/%m/%d}/{}'.format(now(), filename)


class Instagram(Postable):
    pass


class InstagramPhoto(TimeStampedMixin):
    photo = models.ImageField(upload_to=get_instagram_photo_path, verbose_name='사진')
    instagram = models.ForeignKey('instagrams.Instagram',
                                  on_delete=models.CASCADE,
                                  related_name='photos',
                                  verbose_name='인스타그램')
