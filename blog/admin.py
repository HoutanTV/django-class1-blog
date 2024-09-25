from django.contrib import admin
from .models import Post, Comment, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent_category']
    search_fields = ['title']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["author", "category", "posted_on"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_mokhafaf', 'user', 'post']
    search_fields = ['text', 'user', 'post']

    def comment_mokhafaf(self, cm):
        return cm
# Register your models here.
