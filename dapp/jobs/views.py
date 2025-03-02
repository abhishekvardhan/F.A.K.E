from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import ProfileForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import JobForm 

def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('home')
    else:
        user_form = UserCreationForm()
        profile_form = ProfileForm()
    return render(request, 'jobs/register.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            return redirect('home')
    else:
        form = JobForm()
    return render(request, 'jobs/create_job.html', {'form': form})

def home(request):
    """
    Renders the home page.
    """
    return render(request, 'jobs/home.html')
@login_required
def user_logout(request):
    logout(request)  # Ends the user's session
    return redirect('register')