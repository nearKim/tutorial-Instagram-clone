from django.contrib import admin

# Register your models here.
from instagrams.models import Instagram, InstagramPhoto

admin.site.register(Instagram)
admin.site.register(InstagramPhoto)