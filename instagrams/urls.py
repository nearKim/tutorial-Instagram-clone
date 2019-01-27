from django.urls import path

from .views import (
    InstagramDeleteView,
    InstagramCreateView,
    InstagramListView,
    InstagramUpdateView
)

app_name = 'instagrams'

urlpatterns = [
    path('', InstagramListView.as_view(), name='feed-list'),
    path('create/', InstagramCreateView.as_view(), name='feed-create'),
    path('update/<int:pk>/', InstagramUpdateView.as_view(), name='feed-update'),
    path('delete/<int:pk>/', InstagramDeleteView.as_view(), name='feed-delete'),
]
