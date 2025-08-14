from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Post
from django.contrib import messages
from django.views.generic.list import ListView


class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        request.user.email = request.POST.get('email', request.user.email)
        request.user.save()
        messages.success(request, 'Profile updated.')
        return redirect('profile')
    return render(request, 'blog/profile.html')
