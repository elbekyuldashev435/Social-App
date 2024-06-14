from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .models import Posts
from .forms import AddPostForm
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