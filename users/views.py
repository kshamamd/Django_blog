from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm, NewForm, StatusCheck, UserUpdateForm, ProfileUpdateForm
from .models import New
from .models import Status


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
    return render(request, 'users/register.html', {'form': form})


# Create your views here. give the path correctly!


def login(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            #return redirect('register')
    else:
        form = UserRegisterForm()
    return render(request, 'users/login.html')


# return redirect('new')


def logout(request):
    return render(request, 'users/logout.html')


@login_required()
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)#this will populate the form with current user info
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)  # this will populate the form with current user info
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)


@login_required
# provide functionality to existing function user have to login to access this page
def new(request):
    if request.method == 'POST':
        fm = NewForm(request.POST)
        if fm.is_valid():
            fm.save()
            print('post method worked')
        messages.success(request, f'request send to administration !')
        return redirect('user_status')
    else:
        fm = NewForm()
        print('get method se aaya hai')
    return render(request, 'users/new.html', {'form': fm})


@login_required
def user_status(request):
    status = Status.objects.filter(user=request.user.id) #context was missing
    return render(request, 'users/user_status.html', {'status': status})

# fm = new(name=name, surname=surname, role=role, number=number, date=date, optional_number=optional_number,
# address=address, reason=reason)
