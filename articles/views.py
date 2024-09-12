from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm, CommentForm

def list_article(request):
    articles = Article.objects.all()
    return render(request, 'articles/list_articles.html', {'articles': articles})

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_articles')
    else:
        form = ArticleForm()
    return render(request, 'articles/formulaire.html', {'form': form})

def edit_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
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

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.comments.filter(active=True)  # Récupération des commentaires actifs
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
            return redirect('article_detail', id=article.id)
    else:
        comment_form = CommentForm()
    return render(request, 'articles/article_detail.html', {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    })
