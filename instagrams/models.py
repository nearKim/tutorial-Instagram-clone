from datetime import datetime, timedelta
from io import BytesIO

from PIL import Image, ExifTags
from django.conf import settings
from django.core.files.base import ContentFile
from django.db import models

# 인스타그램 사진을 업로드하면 저장할 경로를 지정한다
from django.utils import timezone
from django.utils.timezone import now

from Instagram_clone.mixins import TimeStampedMixin, Postable


def get_instagram_photo_path(instance, filename):
    return 'media/feed/{:%Y/%m/%d}/{}'.format(now(), filename)


def rotate_and_resize(photo):
    # 저장시 가로 최고 길이는 614px이다.
    base = 614
    photo = Image.open(photo)
    photo_format = photo.format

    # exif 태그를 검색하여 사진의 회전여부를 판단한다.
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = dict(photo._getexif().items())

        if exif[orientation] == 3:
            photo = photo.rotate(180, expand=True)
        elif exif[orientation] == 6:
            photo = photo.rotate(270, expand=True)
        elif exif[orientation] == 8:
            photo = photo.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError):
        # 사진에 exif 태그가 없으면 그대로 진행한다.
        pass
    # 회전 컨트롤이 완료된 이미지의 크기를 얻는다.
    (width, height) = photo.size

    # 사진이 작든 크든 너비를 614px로 맞추기 위한 비율을 구한다.
    factor = base / width

    # 너비와 높이를 해당 factor를 곱하여 계산한다.
    photo = photo.resize((int(width * factor), int(height * factor)), Image.ANTIALIAS)
    photo_io = BytesIO()
    photo.save(photo_io, photo_format, quality=60)
    return photo_io


class Instagram(Postable):
    @property
    def timedelta_string(self):
        # settings에서 Timezone을 'Asia/Seoul'로 변경했을 경우 now()는 로컬타임이지만 DB에 저장된 객체들의 시간은 UTC이다.
        # 차이값을 구하기위해 timezone을 맞춰준다. 이 때 datetime의 timezone이 아닌 django.utils의 timezone을 사용한다.
        delta = datetime.now(tz=timezone.utc) - self.created

        if delta < timedelta(minutes=1):
            return str(delta.seconds) + ' 초 전'
        elif delta < timedelta(hours=1):
            return str(delta.seconds / 60) + ' 분 전'
        elif delta < timedelta(days=1):
            return str(delta.seconds / 3600) + ' 시간 전'
        elif delta < timedelta(days=7):
            # TODO: 만일 로컬시간 기준으로 2월 3일 오전 6시에 2월 1일 오후 9시에 작성된 게시글을 볼 경우,
            #  33시간 전이므로 이를 내림한 '1일 전'으로 표시된다. 일반적으로 이경우 2일 전으로 표시한다.
            return str(delta.days) + ' 일 전'
        else:
            return timezone.localtime(self.created, timezone.get_current_timezone())


class InstagramPhoto(TimeStampedMixin):
    photo = models.ImageField(upload_to=get_instagram_photo_path, verbose_name='사진')
    instagram = models.ForeignKey('instagrams.Instagram',
                                  on_delete=models.CASCADE,
                                  related_name='photos',
                                  verbose_name='인스타그램')

    def save(self, *args, **kwargs):
        photo_io = rotate_and_resize(self.photo)
        self.photo.save(self.photo.name, ContentFile(photo_io.getvalue()), save=False)
        # 직접 인스턴스의 save를 불러서 파일을 저장한다.
        super(InstagramPhoto, self).save(*args, **kwargs)
