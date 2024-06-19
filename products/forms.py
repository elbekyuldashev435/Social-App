from django import forms
from .models import Posts, Share, Comment


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('topic', 'post_title', 'post_image', 'post_video', 'post_description')


class ShareForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = ('receiver',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment','star_given')
