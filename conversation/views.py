from django.shortcuts import render
from django.views import View

from .models import Contacts, Messages
# Create your views here.


class MessagesListView(View):
    def get(self, request):
        sent_message = Messages.objects.filter(sender=request.user).order_by('-sent_time')
        received_message = Messages.objects.filter(receiver__contact_user=request.user).order_by('-sent_time')
        for i in received_message:
            print(i.sender.username)
        context = {
            'sent_messages': sent_message,
            'received_messages': received_message
        }
        return render(request, 'message_list.html', context=context)