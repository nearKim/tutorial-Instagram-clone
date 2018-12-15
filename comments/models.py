from django.conf import settings
from django.db import models

from Instagram_clone.mixins import Postable, TimeStampedMixin


class Comment(Postable):
    instagram = models.ForeignKey('instagrams.Instagram',
                                  on_delete=models.CASCADE,
                                  related_name='comments',
                                  verbose_name='인스타그램')
