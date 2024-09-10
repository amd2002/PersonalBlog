from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.contrib.auth.models import User  # Import du modèle User
from .models import Profile
from .forms import ProfileForm

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('list_articles')

    def form_valid(self, form):
        user = form.save()  # Crée un nouvel utilisateur
        login(self.request, user)  # Connecte automatiquement l'utilisateur après inscription
        return redirect(self.success_url)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('edit_profile')

    def get_object(self):
        return self.request.user.profile

    def form_valid(self, form):
        # Sauvegarde le username dans le modèle User
        user = self.request.user
        user.username = form.cleaned_data['username']  # Mets à jour le username
        user.save()  # Sauvegarde l'utilisateur
        form.save()  # Sauvegarde le profil
        return super().form_valid(form)


