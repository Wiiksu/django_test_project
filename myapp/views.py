from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm


def main_page(request):
    return render(request, "myapp/main_page.html")


def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("myapp:user_list")
    else:
        form = UserForm()

    return render(request, "myapp/create_user.html", {"form": form})


def user_list(request):
    users = User.objects.all()
    return render(request, "myapp/user_list.html", {"users": users})
