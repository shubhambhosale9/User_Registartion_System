from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from mysite.core.forms import SignUpForm
from .models import User
User = get_user_model()

def home(request):
    #count = User.objects.count()
    #user = User.objects.all()
    #return render(request, 'home.html', {
    #    'count': count, 'user': user
    #})
    users = User.objects.all()
    count = User.objects.count()
    return render(request, 'home.html', {
        'count' : count, 'users':users
    })


def get(request):
    form = SignUpForm()
    user = User.objects.all()
    print(user)
    args = {'form': form, 'user':user}
    return render(request, 'registration/profile.html', args)

def signup(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            #handle_uploaded_file(request.FILES['file'])
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            return redirect('home')
    else:
        form = SignUpForm()
        #form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


def handle_uploaded_file(f):
    with open('/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@login_required
def secret_page(request):
    users = User.objects.all()
    return render(request, 'secret_page.html', {'users':users})


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'
