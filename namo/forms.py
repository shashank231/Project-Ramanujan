from django.contrib.auth.forms import UserCreationForm             # this is django's default user creation form
from django.contrib.auth.models import User                        # this is django default user model
from.models import *
from django.forms import ModelForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User                                               # jo humne upar import kia hai
        fields = ['username', 'email', 'password1', 'password2']   # these ae called like this in documentation
                                                                   # ab bus yahi fiedls register page me dikhegi

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'phone', 'note']

