from django.urls import path
from .views import (
    CommentDeleteView,
    CommentCreateAjaxView,
    CommentUpdateView
)
app_name = 'comments'

urlpatterns = [
    # 주의! 댓글을 create할 때는 댓글을 작성하려는 'Instagram'객체를 찾아야 하므로 feed_pk를 사용한다.
    path('create/<int:feed_pk>/', CommentCreateAjaxView.as_view(), name='comment-create'),
    # 나머지 경우 댓글 자체를 업데이트하거나 삭제하기 때문에 그대로 comment의 pk를 사용한다.
    path('update/<int:pk>/', CommentUpdateView.as_view(), name='comment-update'),
    path('delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
]
