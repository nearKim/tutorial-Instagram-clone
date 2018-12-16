from django.shortcuts import render

# Create your views here.
from django.views.generic import DeleteView

from instagrams.models import Instagram


class InstagramDeleteView(DeleteView):
    model = Instagram