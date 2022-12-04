from django.shortcuts import render, redirect
from django.contrib import messages


def register(request):
    # Register User
    if request.method == 'POST':
        messages.error(request, 'Testing error message')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # Login User
        return
    else:
        return render(request, 'accounts/register.html')


def logout(request):
    return redirect(request, 'index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
