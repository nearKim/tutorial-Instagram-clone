from django.http import HttpResponseRedirect
from django.views.generic import (
    DeleteView,
    CreateView,
    UpdateView
)

from comments.models import Comment
from instagrams.models import Instagram


class CommentCreateView(CreateView):
    model = Comment
    fields = ['content']
    # TODO: 템플릿 작성
    template_name = 'comments/comments_container.html'

    def form_valid(self, form):
        # 잠깐 db 저장을 멈춘다
        comment = form.save(commit=False)
        # 현재 request를 요청한 user를 댓글의 작성자로 넣어준다
        comment.author = self.request.user
        # 현재 댓글이 달릴 instagram 객체의 pk는 routing rule의 <int:feed_pk>로 넘어온다
        comment.instagram = Instagram.objects.get(pk=self.kwargs.get('feed_pk'))
        comment.save()
        # 댓글을 생성한 이후 댓글을 달고 있었던 request url로 리다이렉트한다.
        return HttpResponseRedirect(self.request.POST.get('next', '/'))


class CommentUpdateView(UpdateView):
    model = Comment
    # TODO: 템플릿 작성
    template_name_suffix = '_update_form'
    fields = ['content']

    def get_success_url(self):
        # 현재 Comment의 absolute_url로 리다이렉트 한다.
        return Comment.objects.get(pk=self.kwargs['pk']).get_absolute_url()


class CommentDeleteView(DeleteView):
    model = Comment

    def get_success_url(self):
        # 이전 페이지로 이동
        # POST request로 넘어온 'next'인자의 값을 읽어서 success_url로 던져준다
        to = self.request.POST.get('next', '/')
        return to
