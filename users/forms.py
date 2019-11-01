from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import VelocityUser

class VelocityUserCreationForm(UserCreationForm):

    class Meta:
        model = VelocityUser
        fields = ('fullname', 'username' , 'email' , 'telephone')


class VelocityUserChangeForm(UserChangeForm):

    class Meta:
        model = VelocityUser
        fields = VelocityUserCreationForm.Meta.fields
