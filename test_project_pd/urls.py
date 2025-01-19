<<<<<<< HEAD
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from test_project_pd import settings
from users.views import CustomLoginView

urlpatterns = [
    # path(r'^admin/login/', views.),
    path("admin/", admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    path("", include("users.urls")),
]

if settings.DEBUG:  # Only serve media files in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
<<<<<<< HEAD
"""
URL configuration for test_project_pd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
=======
from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', views.home, name='home'),
>>>>>>> 9006665 (Initial commit)
]
>>>>>>> dc1f4132362026a9f0402b8b11dd257e05e6c0df
