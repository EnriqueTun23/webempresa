from django.contrib import admin
from .models import Category, Post
from django.utils.safestring import mark_safe

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    # si quiero dejarlo solo por autor lo dejaria 
    # ordering = ('author',) <--- de esta manera
    ordering = ('author', 'published')
    # Se pone las barras para poder buscar en la categoria la subcategoria
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories')

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "CAtegorias"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)