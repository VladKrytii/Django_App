from django.urls import path
<<<<<<< HEAD

from users import views

urlpatterns = [
    path("", views.index),
    path("catalog/", views.catalog),
=======
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
>>>>>>> dc1f4132362026a9f0402b8b11dd257e05e6c0df
    path("create/", views.create),
    path("edit/<int:id>", views.edit),
    path("details/<int:id>", views.details),
    path("delete/<int:id>", views.delete),
<<<<<<< HEAD
]
=======
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', views.home, name='home'),
]


>>>>>>> 9006665 (Initial commit)
>>>>>>> dc1f4132362026a9f0402b8b11dd257e05e6c0df
