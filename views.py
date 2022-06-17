from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse

from django.views.generic import ListView, CreateView, DeleteView, View
from django.contrib import messages

# Main Page
from django.views.generic.list import BaseListView

from mentor.forms import LoginForm, RegistrationForm
from mentor.models import Testimonials


def index(request):
    return render(request, 'blog/index.html')


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')


def course_details(request):
    return render(request, 'blog/course-details.html')


def courses(request):
    return render(request, 'blog/courses.html')


def events(request):
    return render(request, 'blog/events.html')


def pricing(request):
    return render(request, 'blog/pricing.html')


def trainers(request):
    return render(request, 'blog/trainers.html')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'blog/profile.html')
    else:
        return HttpResponse(status=403)


# User Form

def user_form(request):
    login_form = LoginForm()
    registration_form = RegistrationForm()

    context = {
        'login_form': login_form,
        'registration_form': registration_form
    }

    return render(request, 'blog/user_form.html', context)


# Login

def user_login(request):
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('index')
    else:
        messages.error(request, 'Incorrect username or password')
        return redirect('user_form')


# Register

def register(request):
    form = RegistrationForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    else:
        errors = form.errors
        messages.error(request, errors)
    return redirect('user_form')


# Logout

def user_logout(request):
    logout(request)
    return redirect('index')


def testimonial(request):
    testimonials = Testimonials.objects.all()
    context = {
        'testimonials': testimonials
    }

    return render(request, 'blog/components/_testimonials.html', context)
