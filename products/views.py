from django.shortcuts import render
from django.views import View

from .models import Posts
# Create your views here.


class PostsListView(View):
    def get(self, request):
        posts = Posts.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'home.html', context)