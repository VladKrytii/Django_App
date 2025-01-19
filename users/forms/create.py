from django import forms
<<<<<<< HEAD
from users.models import Role, User

class CreateUser(forms.ModelForm):
    
    class Meta:
        model = User
        fields = "__all__"  # all User model fields
        widgets = {
            'role': forms.Select(attrs={'class': 'form-select'}),
        }
     
       
=======
from users.models import User


class CreateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"  # all User model fields
>>>>>>> dc1f4132362026a9f0402b8b11dd257e05e6c0df
