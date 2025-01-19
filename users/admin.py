from django.contrib import admin

<<<<<<< HEAD
from users.models import Product, User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'phone', 'role']
    search_fields = ['name', 'email', 'phone']
    list_filter = ['role']

admin.site.register(User, UserAdmin)
=======
# Register your models here.
>>>>>>> dc1f4132362026a9f0402b8b11dd257e05e6c0df
