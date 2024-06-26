from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from . import forms
from . import models
from django.views import View
from products.models import Posts
from conversation.models import Contacts
from django.contrib import messages


# auth
class Registration(View):
    def get(self, request):
        registration_form = forms.RegistrationForm()
        context = {
            'registration_form': registration_form
        }
        return render(request, 'registration.html', context=context)

    def post(self, request):
        registration_form = forms.RegistrationForm(data=request.POST, files=request.FILES)
        if registration_form.is_valid():
            print(f"{request.user} is valid")
            registration_form.save()
            return redirect('users:login')
        else:
            context = {
                'registration_form': registration_form
            }
            print(f'user -{request}  invalid')
            return render(request, 'registration.html', context=context)


class Login(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'login.html', context=context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            account = login_form.get_user()
            login(request, account)
            return redirect('products:posts-list')

        else:
            context = {
                'login_form': login_form
            }
            return render(request, 'login.html', context=context)


class Logout(View, LoginRequiredMixin):
    def get(self, request):
        logout(request)
        return redirect('products:posts-list')


# profile
class MyProfile(View):
    def get(self, request, pk):
        my_profile = models.Users.objects.get(pk=pk)
        posts = Posts.objects.filter(user=my_profile)
        context = {
            'my_profile': my_profile,
            'posts': posts
        }
        return render(request, 'my_profile.html', context=context)


class Profile(View):
    def get(self, request, pk):
        profile = models.Users.objects.get(pk=pk)
        posts = Posts.objects.filter(user=profile)
        context = {
            'profile': profile,
            'posts': posts
        }
        return render(request, 'profile.html', context=context)


class EditProfile(View):
    def get(self, request, pk):
        profile = models.Users.objects.get(pk=pk)
        edit_profile_form = forms.EditProfileForm(instance=profile)
        context = {
            'edit_profile_form': edit_profile_form
        }
        return render(request, 'edit_profile.html', context=context)

    def post(self, request, pk):
        profile = models.Users.objects.get(pk=pk)
        edit_profile_form = forms.EditProfileForm(request.POST, instance=profile)
        if edit_profile_form.is_valid():
            user = edit_profile_form.save(commit=False)
            password = edit_profile_form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            return redirect('my_profile', pk=profile.pk)
        else:
            context = {
                'edit_profile_form': edit_profile_form
            }
            return render(request, 'edit_profile.html', context=context)


class AddContactView(View):
    def post(self, request, pk):
        user = models.Users.objects.get(pk=pk)
        if not Contacts.objects.filter(main_user=request.user, contact_user__pk=pk):
            Contacts.objects.create(main_user=request.user, contact_user=user)
            messages.success(request, f'Contact "{user.username}" was added successfully.')
        return redirect('users:profile', pk=pk)