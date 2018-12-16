from django.shortcuts import render
from django.views.generic import DeleteView

from comments.models import Comment


class CommentDeleteView(DeleteView):
    model = Comment

    def get_success_url(self):
        # 이전 페이지로 이동
        # POST request로 넘어온 'next'인자의 값을 읽어서 success_url로 던져준다
        to = self.request.POST.get('next', '/')
        return to