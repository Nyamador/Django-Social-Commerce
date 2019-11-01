from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import VelocityUserCreationForm, VelocityUserChangeForm
from .models import  VelocityUser


class VelocityUserAdmin(UserAdmin):
    model = VelocityUser
    add_form = VelocityUserCreationForm
    form = VelocityUserChangeForm


admin.site.register(VelocityUser, VelocityUserAdmin)
