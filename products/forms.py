from django import forms
from .models import Posts, Share


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('topic', 'post_title', 'post_image', 'post_video', 'post_description')


class ShareForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = ('receiver',)