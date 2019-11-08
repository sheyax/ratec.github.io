from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Photo, Profile
from .forms import PhotoForm , UpForm 
from django.views.generic import CreateView



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'usersworks/register.html', {'form':form})

@login_required
def profile(request):
    profiles = Profile.objects.all()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render (request, "usersworks/profile.html", context)


def photo_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        forma= PhotoForm(request.POST, request.FILES)
        if forma.is_valid():
            forma.save()
            return redirect('photo_list')
    else:
        forma= PhotoForm()
        
    context = {
        's_form': forma,
        'photos': photos
    }
    return render(request, "usersworks/profile.html", {'form': form, 'photos': photos})


