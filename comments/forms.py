from django.forms import ModelForm

from comments.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        # 최대한 Instagram과 비슷하게 스타일링한다
        self.fields['content'].widget.attrs['id'] = 'textfield-comment'
        self.fields['content'].widget.attrs['placeholder'] = '댓글 달기...'
        self.fields['content'].label = ''
        # FIXME: 필요에 따라 Text필드가 너무 넓어보인다면 한줄로 제한한다.
        # self.fields['content'].widget.attrs['rows'] = 1
