from django.urls import path

from .views import chat_view, OutboxView, OutboxDetailView, InboxView, InboxDetailView, ContactsListView, AddContactView
from .views import DeleteContactView, AddMessageView

app_name = 'conversation'
urlpatterns = [
    path('chat-view/', chat_view, name='chat-view'),
    path('chats/outbox', OutboxView.as_view(), name='outbox'),
    path('outbox-detail/<int:pk>/', OutboxDetailView.as_view(), name='outbox-detail'),
    path('chats/inbox', InboxView.as_view(), name='inbox'),
    path('inbox-detail/<int:pk>/', InboxDetailView.as_view(), name='inbox-detail'),

    path('contacts-list/', ContactsListView.as_view(), name='contacts-list'),
    path('add-contact/', AddContactView.as_view(), name='add-contact'),
    path('delete-contact/<int:pk>/', DeleteContactView.as_view(), name='delete-contact'),

    path('send-message/<int:pk>/', AddMessageView.as_view(), name='send-message'),
]