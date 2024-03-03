from django.contrib import admin
from blog.models import Post

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'publicado']
    list_display_links = ['id', 'titulo']
    list_filter = ['categorias']


admin.site.register(Post, BlogAdmin)