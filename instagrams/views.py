from django.shortcuts import render

# Create your views here.
from django.views.generic import DeleteView, ListView
from django.views.generic.edit import FormMixin, CreateView, UpdateView

from comments.forms import CommentForm
from instagrams.models import Instagram, InstagramPhoto


class InstagramCreateView(CreateView):
    def form_valid(self, form):
        # 잠깐 save를 막고 현재 user를 author로 넣어준다
        instagram = form.save(commit=False)
        instagram.author = self.request.user
        instagram.save()

        # 만일 requst로 FILE이 넘어온다면 InstagramPhoto로 간주하고 객체들을 생성한다
        if self.request.FILES:
            # forms.py에서 images라는 이름으로 FileField를 정의했음을 기억한다
            for f in self.request.FILES.getlist('images'):
                feed_photo = InstagramPhoto(instagram=instagram, photo=f)
                feed_photo.save()
        # 수퍼클래스의 form_valid 구현을 따로 수정할 필요는 없다.
        return super(InstagramCreateView, self).form_valid(form)


class InstagramListView(FormMixin, ListView):
    form_class = CommentForm
    paginate_by = 20
    # TODO: 템플릿 작성
    template_name = 'instagram/feed_list.html'

    def get_context_data(self, **kwargs):
        # superclass의 get_context_data를 부른다
        context = super(InstagramListView, super).get_context_data(**kwargs)
        # CommentForm을 context_data에 넣어준다
        context['comment_form'] = self.get_form()
        return context

    def get_queryset(self):
        # Instagram 객체들을 가져오는데 FK에 대한 joining을 모조리 해서 가져온다.
        # Reverse relationship을 join해서 가져오기 위해 2번의 prefetch_related를 한다
        # 마지막으로 단순 FK를 join해서 가져오기 위해 1번의 select_related를 한다
        # 최신 객체가 가장 위에 올라와야 하고 그다음으로는 최근 수정된 순으로 객체를 뿌려줘야 한다.
        queryset = Instagram.objects \
            .prefetch_related('photos') \
            .prefetch_related('comments__author') \
            .select_related('author') \
            .order_by('-created', '-updated')
        return queryset


class InstagramUpdateView(UpdateView):
    pass


class InstagramDeleteView(DeleteView):
    model = Instagram
