from django.urls import path

from .views import (
    InstagramDeleteView,
)
app_name = 'instagrams'

urlpatterns = [
    # TODO: CBV들을 작성한다.
    path('', InstagramListView.as_view(), name='feed-list'),
    path('create/', InstagramCreateView.as_view(), name='feed-create'),
    path('update/<int:pk>/', InstagramUpdateView.as_view(), name='feed-update'),
    path('delete/<int:pk>/', InstagramDeleteView.as_view(), name='feed-delete'),
]