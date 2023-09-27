from ast import If
from logging import exception
from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    NewUserForm,
    LoginForm,
    UpdateAuthorForm,
    UpdateVerifForm,
    UpdateAdminForm,
)
from main.models import Author, Verifikator, Administrator
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.contrib import messages
from .models import User
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token

# Create your views here.


def register(request):
    # print( request.method == "POST" )
    form = NewUserForm(request.POST or None)
    ermessages = ""
    if request.method == "POST":
        email = form.data["email"]
        try:
            emailcount = (
                User.objects.filter(email=email).exclude(role="VERIFIKATOR").count()
            )
        except:
            pass
        if emailcount == 1:
            ermessages = "email already exists"
            pass
        else:
            if form.is_valid():
                user = form.save(commit=False)
                user.is_verified = False
                user.save()
                activateEmail(request, user, form.cleaned_data.get("email"))
                auth_login(request, user)
                return redirect("users:update-profile")
    else:
        form = NewUserForm()
        return render(request, "user-auth/register.html", {"form": form})

    # form = NewUserForm()
    context = {"form": form, "ermessages": ermessages}
    return render(request, "user-auth/register.html", context)


def activateEmail(request, user, to_email):
    mail_subject = "Aktifkan akun anda"
    message = render_to_string(
        "user-auth/template_activate_account.html",
        {
            "user": user.username,
            "domain": get_current_site(request).domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user),
            "protocol": "https" if request.is_secure() else "http",
        },
    )
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(
            request,
            f"Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
            received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.",
        )
    else:
        messages.error(
            request,
            f"Problem sending confirmation email to {to_email}, check if you typed it correctly.",
        )


def activate(request, uidb64, token):

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_verified = True
        user.save()

        messages.success(
            request,
            "Thank you for your email confirmation. Now you can login your account.",
        )
        return redirect("index")
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect("index")


def login(request):
    context = {}
    user = request.user

    if user.is_authenticated:
        return redirect("index")

    form = LoginForm(request, data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=user, password=password)
            auth_login(request, user)
            if user is not None:
                return redirect("index")
    else:
        form = LoginForm()
        context = {"title": "Login", "section": "Login", "form": form}
        return render(request, "user-auth/login.html", context)

    context = {"title": "Login", "section": "Login", "form": form}
    return render(request, "user-auth/login.html", context)


# def update_profile(request):

#     context = {
#         "title": "Login",
#         "section": "Login",
#     }
#     return render(request, "user-auth/update-profile.html", context)


@login_required
def update_profile(request):
    context = {}
    user = request.user

    try:
        author = Author.objects.get(user_id=user.id)
        if author.user_id == user.id:
            operation = "edit"
    except Author.DoesNotExist:
        pass

    try:
        verifikator = Verifikator.objects.get(user_id=user.id)
        if verifikator.user_id == user.id:
            operation = "edit"
    except Verifikator.DoesNotExist:
        pass

    try:
        administrator = Administrator.objects.get(user_id=user.id)
        if administrator.user_id == user.id:
            operation = "edit"
    except Administrator.DoesNotExist:
        pass
    # author = get_object_or_404(Author, user_id=user.id)
    # id_user = user.id

    try:
        if user.role == "USER":
            obj = get_object_or_404(Author, user=user)
            form = UpdateAuthorForm(request.POST, request.FILES, instance=obj)
        elif user.role == "VERIFIKATOR":
            obj = get_object_or_404(Verifikator, user=user)
            form = UpdateVerifForm(request.POST, request.FILES, instance=obj)
        else:
            obj = get_object_or_404(Administrator, user=user)
            form = UpdateAdminForm(request.POST, request.FILES, instance=obj)
    except:
        if user.role == "USER":
            # obj = get_object_or_404(Author, user=user)
            form = UpdateAuthorForm(request.POST, request.FILES)
        elif user.role == "VERIFIKATOR":
            form = UpdateVerifForm(request.POST, request.FILES)
        else:
            form = UpdateAdminForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            update_profile = form.save(commit=False)
            update_profile.user = user
            update_profile.save()
            return redirect("profil")
    context = {
        "title": "Update Profile",
        "section": "Update Profile",
        "form": form,
    }
    return render(request, "user-auth/update-profile.html", context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect("index")
