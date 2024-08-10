from django.shortcuts import render, get_object_or_404
from .models import Article

def all_blogs(request):
    articles = Article.objects.all()
    return render(request, 'blog/all_blogs.html', {'articles':articles})

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/article.html', {'article':article})
