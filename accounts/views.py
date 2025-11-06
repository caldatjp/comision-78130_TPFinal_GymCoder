from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from accounts.forms import PerfilChangeForm, PerfilCreationForm


def register(request):
    if request.method == "POST":
        form = PerfilCreationForm(request.POST, request.FILES) # request.FILES
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile_detail')
    else:
        form = PerfilCreationForm()
    return render(request, "accounts/register.html", {"form": form})


@login_required           # class ProfileDetail(login_required):
def profile_detail(request):
    return render(request, "accounts/profile_detail.html", {"user": request.user})

@login_required
def profile_edit(request):
    if request.method == "POST":
        form = PerfilChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile_detail")
    else:
        form = PerfilChangeForm(instance=request.user)
    return render(request, "accounts/profile_edit.html", {"form": form})


from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect

def cambiar_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("profile_detail")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "accounts/password_change.html", {"form": form})
