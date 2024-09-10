from django.urls import path
from .views import list_article, create_article,edit_article,delete_article,article_detail

urlpatterns = [
    path('', list_article, name='list_articles'),
    path('nouveau/', create_article, name='create_article'),
    path('edit/<int:id>/',edit_article, name ='edit_article'),
    path ('delete/<int:id>/', delete_article, name='delete_article'),
    path('<int:id>/', article_detail, name='article_detail'),  
]
