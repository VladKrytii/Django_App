<<<<<<< HEAD
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib import messages
=======
from django.http import HttpResponse
<<<<<<< HEAD
from django.shortcuts import render

users = [
    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {"lat": "-37.3159", "lng": "81.1496"},
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets",
        },
    },
    {
        "id": 2,
        "name": "Ervin Howell",
        "username": "Antonette",
        "email": "Shanna@melissa.tv",
        "address": {
            "street": "Victor Plains",
            "suite": "Suite 879",
            "city": "Wisokyburgh",
            "zipcode": "90566-7771",
            "geo": {"lat": "-43.9509", "lng": "-34.4618"},
        },
        "phone": "010-692-6593 x09125",
        "website": "anastasia.net",
        "company": {
            "name": "Deckow-Crist",
            "catchPhrase": "Proactive didactic contingency",
            "bs": "synergize scalable supply-chains",
        },
    },
    {
        "id": 3,
        "name": "Clementine Bauch",
        "username": "Samantha",
        "email": "Nathan@yesenia.net",
        "address": {
            "street": "Douglas Extension",
            "suite": "Suite 847",
            "city": "McKenziehaven",
            "zipcode": "59590-4157",
            "geo": {"lat": "-68.6102", "lng": "-47.0653"},
        },
        "phone": "1-463-123-4447",
        "website": "ramiro.info",
        "company": {
            "name": "Romaguera-Jacobson",
            "catchPhrase": "Face to face bifurcated interface",
            "bs": "e-enable strategic applications",
        },
    },
]
=======
from django.shortcuts import redirect, render
>>>>>>> dc1f4132362026a9f0402b8b11dd257e05e6c0df

from users.forms.create import CreateUser
from users.forms.edit import EditUser
from users.models import User
<<<<<<< HEAD

def index(request):
=======
>>>>>>> 9006665 (Initial commit)


# Create your views here.
def home(request):
<<<<<<< HEAD
    return HttpResponse("Hello, World!")


def list(request):
    html = "<h1>Users</h1> <ul>"
    for user in users:
        html += f"<li>{user['name']}</li>"
    html += "</ul>"

    return HttpResponse(html)


def details(request, id):
    return HttpResponse(f"User - {id}]!")
=======
    return HttpResponse("<h1>Hello, World!</h1>")

def home(request):
>>>>>>> dc1f4132362026a9f0402b8b11dd257e05e6c0df
    users = User.objects.all()
    return render(request, "index.html", {"users": users})


<<<<<<< HEAD
def catalog(request):
    users = User.objects.all()
    return render(request, "catalog.html", {"users": users})
=======

def list(request):
    users = User.objects.all()
    return render(request, "index.html", {"users": users})
>>>>>>> dc1f4132362026a9f0402b8b11dd257e05e6c0df


def details(request, id):
    user = User.objects.get(id=id)
    # TODO: check if user exists

<<<<<<< HEAD
    return render(request, "details.html", {
        "user": {
            **model_to_dict(user),
            "roleName": User.ROLE_CHOICES[user.role][1]
        }, 
        "return_url": "/"})
=======
    return render(request, "details.html", {"user": user})
>>>>>>> dc1f4132362026a9f0402b8b11dd257e05e6c0df


def create(request):

    form = CreateUser()

    if request.method == "POST":
<<<<<<< HEAD
        form = CreateUser(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, "User created successfully!")
            return redirect("/")
        else:
            messages.error(request, "Invalid data!")

    return render(request, "create.html", {"form": form, "return_url": "/", "roles": User.ROLE_CHOICES})
=======
        form = CreateUser(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/users")

    return render(request, "create.html", {"form": form})
>>>>>>> dc1f4132362026a9f0402b8b11dd257e05e6c0df


def edit(request, id):

    user = User.objects.get(id=id)

    if user is None:
        return HttpResponse("User not found")

    form = EditUser(instance=user)

    if request.method == "POST":
<<<<<<< HEAD
        form = CreateUser(request.POST, request.FILES, instance=user)

        if request.FILES and user.avatar: # do work when avatar != None, 0, False, "", [], (), {}
            user.avatar.delete()

        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, "edit.html", {"form": form, "return_url": "/"})
=======
        form = CreateUser(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect("/users")

    return render(request, "edit.html", {"form": form})
>>>>>>> dc1f4132362026a9f0402b8b11dd257e05e6c0df


def delete(request, id):
    user = User.objects.get(id=id)

    if user is None:
        return HttpResponse("User not found")

<<<<<<< HEAD
    if user.avatar: # do work when avatar != None, 0, False, "", [], (), {}
        user.avatar.delete()
        
    user.delete()

    return redirect("/")


class CustomLoginView(LoginView):
    # template_name = 'login.html'
    # authentication_form = CustomAuthenticationForm

    def form_valid(self, form):
        # Add your authentication logic here
        return super().form_valid(form)
=======
    user.delete()

    return redirect("/users")
>>>>>>> 9006665 (Initial commit)
>>>>>>> dc1f4132362026a9f0402b8b11dd257e05e6c0df
