from django.db import models
from django.utils import timezone


#title, contenu, 

class Article(models.Model):
    title = models.CharField(max_length=225)
    summary = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    date_pub = models.DateField(null=True, blank=True)  # ou auto_now_add=True
    image = models.ImageField(upload_to='articles_images/', null=True, blank=True)

    
    def __str__(self):
          return self.title
   

    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')  # Clé étrangère reliant chaque commentaire à un article spécifique. Si l'article est supprimé, les commentaires associés le seront aussi.
    name = models.CharField(max_length=80)  # Champ pour le nom de la personne qui laisse le commentaire
    email = models.EmailField()  # Champ pour l'email de la personne qui laisse le commentaire
    body = models.TextField()  # Champ pour le contenu du commentaire
    created_on = models.DateTimeField(default=timezone.now)  # Date et heure de création du commentaire
    active = models.BooleanField(default=True)  # Champ booléen pour activer ou désactiver l'affichage du commentaire
    

    class Meta:
        ordering = ['-created_on']  # Classe les commentaires par date de création décroissante

    def __str__(self):
        return f'Comment by {self.name} on {self.article}'  # Affiche le nom de la personne et l'article associé lors de l'affichage de l'objet