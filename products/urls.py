from django.urls import path
<<<<<<< HEAD
from .views import PostsListView, AddPostView, SharePostView, choice_view, OutboxShareView, InboxShareView, PostDetailView
from .views import SavePostView, DeleteSaveView
=======
from .views import PostsListView, AddPostView, SharePostView, choice_view, OutboxShareView, InboxShareView, \
    PostDetailView, AddComment, like_post
from .views import SavePostView
>>>>>>> be48ec084c74d7442947570ffd27401e1a605e65

app_name = 'products'
urlpatterns = [
    path('', PostsListView.as_view(), name='posts-list'),
    path('post-detail/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('share-post/<int:pk>', SharePostView.as_view(), name='share-post'),

    path('choice/', choice_view, name='choice'),
    path('outbox-share/', OutboxShareView.as_view(), name='outbox-share'),
    path('inbox-share/', InboxShareView.as_view(), name='inbox-share'),

    path('saved-posts/', SavePostView.as_view(), name='saved-posts'),
    path('save-post/<int:pk>/', SavePostView.as_view(), name='save-post'),
<<<<<<< HEAD
    path('delete-saved/<int:pk>/', DeleteSaveView.as_view(), name='delete-saved')
=======

    path('comments/<int:pk>/', AddComment.as_view(), name='comments'),
    path('like-post/<int:pk>/', like_post, name='like-post'),

>>>>>>> be48ec084c74d7442947570ffd27401e1a605e65
]