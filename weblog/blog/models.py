from django.db import models
from django.utils import timezone
from django.utils.html import format_html


# my managers
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    status = models.BooleanField(default=True)
    position = models.IntegerField()

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published')
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ManyToManyField(Category, related_name="articles")
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        ordering = ['-publish']

    def __str__(self) -> str:
        return self.title

    def active_categories(self):
        return self.category.filter(status=True)
    
    def thumbnail_tag(self):
        return format_html(f"<img style='width: 100px; height: 75px; border-radius: 5px;' src='{self.thumbnail.url}'>")
    thumbnail_tag.short_description = "Thumbnail"

    objects = ArticleManager()  # My manager
