from django.contrib import admin
from .models import Article, Category


def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated == 1:
        message_bit = "1 article was"
    else:
        message_bit = "%s articles were" % rows_updated
    modeladmin.message_user(request, "%s successfully marked as published." % message_bit)
make_published.short_description = "Mark selected articles as published"


def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status='d')
    if rows_updated == 1:
        message_bit = "1 article was"
    else:
        message_bit = "%s articles were" % rows_updated
    modeladmin.message_user(request, "%s successfully marked as draft" % message_bit)
make_draft.short_description = "Mark selected articles as draft"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish', 'status', 'cat_to_str']
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', '-publish']
    actions = [make_published, make_draft]

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