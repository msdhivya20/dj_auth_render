from django.shortcuts import render,redirect

from django.contrib import messages

from django.contrib.auth import (login,logout,authenticate)

from django.contrib.auth.forms import (AuthenticationForm)

from django.contrib.auth.decorators import (login_required)

from .forms import RegisterForm

from .models import Profile

def home(request):

    return render(
        request,
        'home.html'
    )


def signup(request):
    
    form=RegisterForm()

    if request.method=="POST":

        form=RegisterForm(
            request.POST
        )

        if form.is_valid():

            user=form.save()

            Profile.objects.create(
                user=user
                )

            messages.success(
                request,
                "Account created successfully"
            )

            login(
                request,
                user
            )

            return redirect(
                'dashboard'
            )
   

    return render(
        request,
        'signup.html',
        {
            'form':form
        }
    )


def login_view(request):

    if request.method=="POST":

        username=request.POST.get(
            'username'
        )

        password=request.POST.get(
            'password'
        )

        user=authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(
                request,
                user
            )

            return redirect(
                'dashboard'
            )

        else:

            messages.error(
                request,
                "Incorrect username or password"
            )

    return render(
        request,
        'login.html'
    )
@login_required
def dashboard(request):

    Profile.objects.get_or_create(
        user=request.user
    )

    return render(
        request,
        'dashboard.html'
    )


def logout_view(request):

    logout(request)

    return redirect(
        'home'
    )

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages


def forgot_username(request):

    if request.method=="POST":

        email=request.POST.get(
            'email'
        )

        try:

            user=User.objects.get(
                email=email
            )

            send_mail(

                'Your Username',

                f'Username: {user.username}',

                None,

                [email]

            )

            messages.success(
                request,
                'Username sent'
            )

        except:

            messages.error(
                request,
                'Email not found'
            )

    return render(
        request,
        'forgot_username.html'
    )



@login_required
def upload_profile(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method=="POST":

        if request.FILES.get('image'):

            profile.image=request.FILES['image']

            profile.save()

            return redirect(
                'dashboard'
            )

    return render(
        request,
        'upload_profile.html'
    )