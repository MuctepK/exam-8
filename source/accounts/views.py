from django.contrib.auth import login
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm
from accounts.models import Profile


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('webapp:index')
    else:
        form = SignUpForm()
    return render(request, 'register.html', context={'form': form})