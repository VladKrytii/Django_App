from django.db import models

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
