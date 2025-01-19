from django.db import models

<<<<<<< HEAD


# Create your models here.
class User(models.Model):
    ROLE_CHOICES = [
        (0, 'Admin'),
        (1, 'User'),
        (2, 'Manager'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatars/")
    role = models.IntegerField(choices=ROLE_CHOICES, default=0)

    list_display = ('name', 'email', 'phone', 'role')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('role')

    # override default table name
    # class Meta:
    #     db_table = 'users'

    def __str__(self):
        return f"{self.name} - {self.email}"

class Role(models.Model):
    name = models.CharField( 
        max_length = 40, 
        choices = User.ROLE_CHOICES, 
        default = 0) 

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to="products/")
=======
<<<<<<< HEAD
# Create your models here.
=======

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name
>>>>>>> 9006665 (Initial commit)
>>>>>>> dc1f4132362026a9f0402b8b11dd257e05e6c0df
