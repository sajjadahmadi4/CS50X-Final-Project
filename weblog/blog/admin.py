from django.contrib import admin
from .models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish', 'status', 'cat_to_str']
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', '-publish']

    def cat_to_str(self, obj):
        return ", ".join([category.title for category in obj.active_categories()])
    cat_to_str.short_description = "CATEGORY"


admin.site.register(Article, ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['position', 'title', 'slug', 'status']
    list_filter = (['status'])
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)