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

from users.forms.create import CreateUser
from users.forms.edit import EditUser
from users.models import User
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
    users = User.objects.all()
    return render(request, "index.html", {"users": users})



def list(request):
    users = User.objects.all()
    return render(request, "index.html", {"users": users})


def details(request, id):
    user = User.objects.get(id=id)
    # TODO: check if user exists

    return render(request, "details.html", {"user": user})


def create(request):

    form = CreateUser()

    if request.method == "POST":
        form = CreateUser(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/users")

    return render(request, "create.html", {"form": form})


def edit(request, id):

    user = User.objects.get(id=id)

    if user is None:
        return HttpResponse("User not found")

    form = EditUser(instance=user)

    if request.method == "POST":
        form = CreateUser(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect("/users")

    return render(request, "edit.html", {"form": form})


def delete(request, id):
    user = User.objects.get(id=id)

    if user is None:
        return HttpResponse("User not found")

    user.delete()

    return redirect("/users")
>>>>>>> 9006665 (Initial commit)
