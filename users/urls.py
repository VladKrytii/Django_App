from django.urls import path
<<<<<<< HEAD

=======
from django.contrib import admin
from django.urls import path, include
>>>>>>> 9006665 (Initial commit)
from users import views

urlpatterns = [
    path("home/", views.home),
<<<<<<< HEAD
    path("list/", views.list),
    path("details/<int:id>", views.details),
]
=======
    path("", views.list),
    path("create/", views.create),
    path("edit/<int:id>", views.edit),
    path("details/<int:id>", views.details),
    path("delete/<int:id>", views.delete),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', views.home, name='home'),
]


>>>>>>> 9006665 (Initial commit)
