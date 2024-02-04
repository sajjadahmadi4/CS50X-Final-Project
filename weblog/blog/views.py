from django.shortcuts import render
from .models import Article


def index(request):
    context = {
        "articles": Article.objects.filter(status='p').order_by('-publish')
    }
    return render(
        request,
        "blog/index.html",
        context
    )

def detail(request, slug):
    context = {
        "article": Article.objects.get(slug=slug)
    }
    return render(request, "blog/detail.html", context)
