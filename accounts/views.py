from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import UserForm, UserProfileForm
from . import models


def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(
                        reverse('accounts:profile_detail', kwargs={
                            'user_pk': user.pk,  # == self.course.pk
                        })
                    )
                else:
                    messages.error(
                        request,
                        "That user account has been disabled."
                    )
            else:
                messages.error(
                    request,
                    "Username or password is incorrect."
                )
    return render(request, 'accounts/sign_in.html', {'form': form})


def sign_up(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))

    user_form = UserForm()
    profile_form = UserProfileForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.bio = profile_form.cleaned_data['bio']
            profile.dob = profile_form.cleaned_data['dob']

            if 'picture' in request.FILES:
                profile.profile_pic = request.FILES['picture']

            profile.save()
            return HttpResponseRedirect(reverse('accounts:profile_detail', kwargs={'profile_pk': profile.pk}))

        else:
            print(user_form.errors, profile_form.errors)

    return render(request, 'accounts/sign_up.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def sign_out(request):
    logout(request)
    messages.success(request, "You've been signed out. Come back soon!")
    return HttpResponseRedirect(reverse('home'))


# PROFILE
@login_required
def profile_detail(request, user_pk):
    user = get_object_or_404(models.User, pk=user_pk)
    return render(request, 'accounts/profile.html', {'user': user})


def profile_edit(request, profile_pk):
    return render(request, 'accounts/edit_profile.html', {'profile': {'name': 'Yuni'}})


def profile_change_password(request, profile_pk):
    return render(request, 'accounts/change_password.html', {'profile': {'name': 'Yuni'}})
