from django import forms
from users.models import User


class EditUser(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"  # all User model fields
<<<<<<< HEAD
        widgets = {
            'role': forms.Select(attrs={'class': 'form-select'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
=======
>>>>>>> dc1f4132362026a9f0402b8b11dd257e05e6c0df
