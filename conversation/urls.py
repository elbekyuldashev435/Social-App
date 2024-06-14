from django.urls import path

from .views import chat_view, OutboxView, OutboxDetailView, InboxView


app_name = 'conversation'
urlpatterns = [
    path('chats/outbox', OutboxView.as_view(), name='outbox'),
    path('outbox-detail/<int:pk>/', OutboxDetailView.as_view(), name='outbox-detail'),
    path('chats/inbox', InboxView.as_view(), name='inbox'),
]