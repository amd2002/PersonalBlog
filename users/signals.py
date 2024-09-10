from django.db.models.signals import post_save  # Import du signal post_save, qui est émis après la sauvegarde d'un objet (ici, un utilisateur).
from django.contrib.auth.models import User  # Import du modèle User fourni par Django pour gérer les utilisateurs.
from django.dispatch import receiver  # Import du décorateur receiver, qui permet de connecter des signaux à des fonctions spécifiques.
from .models import Profile  # Import du modèle Profile que nous avons défini pour étendre les informations utilisateur.

# Cette fonction est un récepteur qui sera appelé chaque fois qu'un nouvel utilisateur (User) est sauvegardé dans la base de données.
@receiver(post_save, sender=User)  # Indique que cette fonction doit être appelée après la sauvegarde d'un objet User.
def create_user_profile(sender, instance, created, **kwargs):
    # Si l'utilisateur est nouvellement créé (et non modifié), on crée un profil associé.
    if created:  # Vérifie si l'objet User a été créé (et non modifié).
        Profile.objects.create(user=instance)  # Crée un profil pour l'utilisateur nouvellement créé.

# Cette fonction est appelée après la sauvegarde d'un utilisateur pour s'assurer que son profil est également sauvegardé.
@receiver(post_save, sender=User)  # Indique que cette fonction doit être appelée après la sauvegarde d'un objet User.
def save_user_profile(sender, instance, **kwargs):
    # Sauvegarde le profil associé à l'utilisateur chaque fois que l'utilisateur est sauvegardé.
    instance.profile.save()  # Appelle la méthode save() sur le profil pour s'assurer qu'il est bien mis à jour.
