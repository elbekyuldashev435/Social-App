from django.urls import path

from .views import MessagesListView


app_name = 'conversation'
urlpatterns = [
    path('', MessagesListView.as_view(), name='message-list')
]