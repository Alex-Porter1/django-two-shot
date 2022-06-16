from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             username = request.POST.get("username")
#             password = request.POST.get("password1")
#             user = User.objects.create_user(
#                 username=username,
#                 password=password,
#             )
#             user.save()
#             login(request, user)
#             return redirect("home")
#     else:
#         form = UserCreationForm()
#     context = {
#         "form": form,
#     }
#     return render(request, "registration/signup.html", context)

def signup(request):
    # run request (when user makes a request on the signup page)
    if request.method == 'POST':
        # UserCreationForm is automatically generated from the import
        form = UserCreationForm(request.POST)
        # if the form inputs are valid
        if form.is_valid():
            # newly create form is saved to user
            user = form.save()
            # login will be passed after request is passed
            # user is the form that was just created and saved
            login(request, user)    # this line basically means, Log in the user that just made this request and create the account
            # returns the user to the home page
            return redirect("home")
    # if they're just visiting this page, they're just directed to the signup page
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
