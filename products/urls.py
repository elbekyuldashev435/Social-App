from django.urls import path
from .views import PostsListView


app_name = 'products'
urlpatterns = [
    path('', PostsListView.as_view(), name='posts-list')
]