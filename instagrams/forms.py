from django.forms import ModelForm, forms, ClearableFileInput

from instagrams.models import Instagram


class InstagramForm(ModelForm):
    class Meta:
        model=Instagram
        fields=['content']

    # 여러개의 FileInput을 허용하는 새로운 'images'필드를 정의한다.
    images = forms.FileField(widget=ClearableFileInput(attrs={'multiple': True}), label='사진')

