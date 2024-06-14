from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .models import Posts, Share
from .forms import AddPostForm, ShareForm
# Create your views here.


class PostsListView(View):
    def get(self, request):
        posts = Posts.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'home.html', context)


class AddPostView(View):
    def get(self, request):
        form = AddPostForm()
        context = {
            'form': form
        }
        return render(request, 'upload_post.html', context=context)

    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Your post was uploaded successfully.')
            return redirect('products:posts-list')
        else:
            return render(request, 'upload_post.html', context={'form': form})


class SharePostView(View):
    def get(self, request,  *args, **kwargs):
        pk = kwargs.get('pk')
        form = ShareForm()
        context = {
            'form': form
        }
        return render(request, 'share_post.html', context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        form = ShareForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.sender = request.user
            post.post = Posts.objects.get(pk=pk)
            post.save()
            messages.success(request, 'Your post was shared successfully.')
            return redirect('products:posts-list')
        else:
            return render(request, 'share_post.html', context={'form': form})


def choice_view(request):
    return render(request, 'choice.html')


class OutboxShareView(View):
    def get(self, request):
        posts = Share.objects.filter(sender=request.user)
        for i in posts:
            print(i.post.post_image)
        context = {
            'posts': posts
        }
        return render(request, 'outbox_share.html', context)