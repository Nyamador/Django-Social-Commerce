# users/views.py
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView

from .forms import VelocityUserCreationForm
from .models import Profile as profile_model

class SignUpView(CreateView):
    form_class = VelocityUserCreationForm
    success_url = reverse_lazy('account_login')
    template_name = 'registration/signup.html'


def Profile(request, id):
    pows = get_object_or_404(profile_model, id=id)

    return render(request, 'users/profile.html', {'pows':pows})