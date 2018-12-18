from django.conf import settings
from django.db import models
from django.urls import reverse

from Instagram_clone.mixins import Postable, TimeStampedMixin


class Comment(Postable):
    instagram = models.ForeignKey('instagrams.Instagram',
                                  on_delete=models.CASCADE,
                                  related_name='comments',
                                  verbose_name='인스타그램')

    def get_absolute_url(self):
        # Instagram feed-list로 리다이렉트한다.
        return reverse('instagrams:feed-list')
