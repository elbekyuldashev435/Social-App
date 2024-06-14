from django.urls import path
from .views import PostsListView, AddPostView, SharePostView, choice_view, OutboxShareView


app_name = 'products'
urlpatterns = [
    path('', PostsListView.as_view(), name='posts-list'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('share-post/<int:pk>/', SharePostView.as_view(), name='share-post'),

    path('choice/', choice_view, name='choice'),
    path('outbox-share/', OutboxShareView.as_view(), name='outbox-share')
]