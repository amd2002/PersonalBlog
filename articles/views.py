#views.py
from django.shortcuts import render,redirect, get_object_or_404
from.models import Article, Comment    # Importation des modèles Article et Comment 
from .forms import ArticleForm, CommentForm        # Importation des fonctions pour rendre les templates et gérer les erreurs 404


def list_article(request):
    arts = Article.objects.all()

    context= {
        'articles': arts
    }
    return render(request, 'articles/list_articles.html', context)


def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)  # Gère les fichiers téléchargés avec request.FILES
        if form.is_valid():
            form.save()
            return redirect('list_articles')
        else:
            print(form.errors)  # Affiche les erreurs du formulaire dans la console (pour déboguer)
    else:
        form = ArticleForm()
    
    return render(request, 'articles/formulaire.html', {'form': form})


def edit_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)  # Gère les fichiers téléchargés avec request.FILES
        if form.is_valid():
            form.save()
            return redirect('list_articles')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/edit_article.html', {'form': form})


def delete_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        article.delete()
        return redirect('list_articles')
    return render(request, 'articles/delete_article.html', {'article': article})


from django.shortcuts import render, get_object_or_404  # Importation des fonctions pour rendre les templates et gérer les erreurs 404
from .models import Article, Comment  # Importation des modèles Article et Comment
from .forms import CommentForm  # Importation du formulaire CommentForm

# Vue pour afficher les détails d'un article spécifique
def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.comments.filter(active=True)  # Récupération des commentaires actifs

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
            return redirect('article_detail', id=article.id)  # Redirection après soumission
    else:
        comment_form = CommentForm()

    return render(request, 'articles/article_detail.html', {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    })
