from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages

from .models import Posts, Share, Save, Comment
from .forms import AddPostForm, ShareForm, CommentForm
from conversation.models import Contacts
# Create your views here.
from random import sample


class PostsListView(View):
    def get(self, request):
        posts = Posts.objects.all().order_by('?')
        context = {
            'posts': posts,
        }
        return render(request, 'home.html', context)


class PostDetailView(View):
    def get(self, request, pk):
        post = Posts.objects.get(pk=pk)
        comment = Comment.objects.filter(post_id=pk)

        context = {
            'post': post,
            'comment': comment,
        }
        return render(request, 'post_detail.html', context=context)


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
    def get(self, request, *args, **kwargs):
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
            post.receiver = Contacts.objects.get(pk=pk)
            post.save()
            messages.success(request, 'Your post was shared successfully.')
            return redirect('products:posts-list')
        else:
            return render(request, 'share_post.html', context={'form': form})


def choice_view(request):
    return render(request, 'choice.html')


class OutboxShareView(View):
    def get(self, request):
        posts = Share.objects.filter(sender=request.user).order_by('-sent_time')
        for i in posts:
            print(i.post.post_image)
        context = {
            'posts': posts
        }
        return render(request, 'outbox_share.html', context)


class InboxShareView(View):
    def get(self, request):
        posts = Share.objects.filter(receiver=request.user).order_by('-sent_time')
        context = {
            'posts': posts
        }
        return render(request, 'inbox_share.html', context=context)


class SavePostView(View):
    def get(self, request):
        saved_items = Save.objects.filter(user=request.user).order_by('-saved_time')
        context = {
            'saved_items': saved_items
        }
        return render(request, 'saved_items.html', context=context)

    def post(self, request, pk):
        post = Posts.objects.get(pk=pk)
        if not Save.objects.filter(post=post, user=request.user).exists():
            Save.objects.create(user=request.user, post=post)
        return redirect('products:posts-list')


<<<<<<< HEAD
class DeleteSaveView(View):
    def post(self, request, pk):
        post = get_object_or_404(Save, post__pk=pk)
        post.delete()
        messages.success(request, f'Post "{post.post.post_title}" was deleted successfully.')
        return redirect('products:saved-posts')
=======
class AddComment(View):
    def get(self, request, pk):
        post = Posts.objects.get(pk=pk)
        addcomment_form = CommentForm()
        context = {
            'post': post,
            'addcomment_form': addcomment_form
        }
        return render(request, 'comment.html', context=context)

    def post(self, request, pk):
        post = Posts.objects.get(pk=pk)
        addcomment_form = CommentForm(request.POST)
        if addcomment_form.is_valid():
            Comment.objects.create(
                comment=addcomment_form.cleaned_data['comment'],
                post=post,
                user=request.user,
                star_given=addcomment_form.cleaned_data['star_given']
            )
            return redirect('products:post-detail', pk=pk)
        context = {
            'post': post,
            'addcomment_form': addcomment_form
        }
        return render(request, 'comment.html', context=context)


from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Posts


@login_required
@require_POST
def like_post(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return JsonResponse({'liked': liked, 'total_likes': post.total_likes})
>>>>>>> be48ec084c74d7442947570ffd27401e1a605e65
