from django.urls import path
from .views import PostsListView, AddPostView


app_name = 'products'
urlpatterns = [
    path('', PostsListView.as_view(), name='posts-list'),
    path('add-post/', AddPostView.as_view(), name='add-post')
]