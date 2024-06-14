from django.shortcuts import render
from django.views import View

from .models import Contacts, Messages
from users.models import Users
# Create your views here.


def chat_view(request):
    return render(request, 'chats.html')


class OutboxView(View):
    def get(self, request):
        outboxes = Messages.objects.filter(sender=request.user).order_by('-sent_time')
        context = {
            'outboxes': outboxes,
        }
        return render(request, 'outbox.html', context=context)


class InboxView(View):
    def get(self, request):
        inboxes = Messages.objects.filter(receiver__contact_user=request.user)
        for i in inboxes:
            print(i)
        context = {
            'inboxes': inboxes,
        }
        return render(request, 'inbox.html', context=context)


class OutboxDetailView(View):
    def get(self, request, pk):
        message = Messages.objects.get(pk=pk)
        context = {
            'message': message
        }
        return render(request, 'outbox_detail.html', context=context)