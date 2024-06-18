from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DeleteView
from django.contrib import messages

from .models import Contacts, Messages
from .forms import AddContactForm, AddMessageForm
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
        inboxes = Messages.objects.filter(receiver__contact_user=request.user).order_by('-sent_time')
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


class InboxDetailView(View):
    def get(self, request, pk):
        message = Messages.objects.get(pk=pk)
        context = {
            'message': message
        }
        return render(request, 'inbox_detail.html', context=context)


class ContactsListView(View):
    def get(self, request):
        contacts = Contacts.objects.filter(main_user=request.user).order_by('name')
        context = {
            'contacts': contacts
        }
        return render(request, 'contacts_list.html', context=context)


class AddContactView(View):
    def get(self, request):
        form = AddContactForm()
        context = {
            'form': form
        }
        return render(request, 'add_contact.html', context=context)

    def post(self, request):
        form = AddContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.main_user = request.user
            contact.save()
            messages.success(request, f'Contact "{contact.name}" was added successfully.')
            return redirect('conversation:contacts-list')
        else:
            context = {
                'form': form
            }
        return render(request, 'add_contact.html', context=context)


class DeleteContactView(View):
    def get(self, request, pk):
        contact = Contacts.objects.get(pk=pk)
        context = {
            'contact': contact
        }
        return render(request, 'delete_contact.html', context=context)

    def post(self, request, pk):
        contact = Contacts.objects.get(pk=pk)
        contact.delete()
        messages.success(request, f'Contact "{contact.name}" was deleted successfully.')
        return redirect('conversation:contacts-list')


class AddMessageView(View):
    def get(self, request, pk):
        contact = Contacts.objects.get(pk=pk)
        form = AddMessageForm()
        context = {
            'contact': contact,
            'form': form
        }
        return render(request, 'add_message.html', context=context)

    def post(self, request, pk):
        contact = Contacts.objects.get(pk=pk)
        form = AddMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = contact
            message.save()
            messages.success(request, f'Message was sent successfully.')
            return redirect('conversation:inbox')
        else:
            context = {
                'contact': contact,
                'form': form
            }
        return render(request, 'add_message.html', context=context)


class DeleteInboxMessageView(View):
    def get(self, request, pk):
        message = Messages.objects.get(pk=pk)
        context = {
            'message': message
        }
        return render(request, 'delete_inbox_message.html', context=context)

    def post(self, request, pk):
        message = Messages.objects.get(pk=pk)
        message.delete()
        messages.success(request, f'Message was deleted successfully.')
        return redirect('conversation:inbox')


class DeleteOutboxMessageView(View):
    def get(self, request, pk):
        message = Messages.objects.get(pk=pk)
        context = {
            'message': message
        }
        return render(request, 'delete_outbox_message.html', context=context)

    def post(self, request, pk):
        message = Messages.objects.get(pk=pk)
        message.delete()
        messages.success(request, f'Message was deleted successfully.')
        return redirect('conversation:outbox')