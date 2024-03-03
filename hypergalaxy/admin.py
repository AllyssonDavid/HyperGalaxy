from django.contrib import admin
from hypergalaxy.models import Projeto, ImagesProject, Funcionario

# Register your models here.
class ProjetosAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'publicado']
    list_display_links = ['id', 'titulo']
    list_filter = ['publicado', 'categoria']

admin.site.register(Projeto, ProjetosAdmin)

class ImagensProjetoAdmin(admin.ModelAdmin):
    list_display = ['id', 'descricao']
    list_display_links = ['id', 'descricao']

admin.site.register(ImagesProject, ImagensProjetoAdmin)

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'cargo']
    list_display_links = ['id', 'nome']
    list_filter = ['cargo']

admin.site.register(Funcionario, FuncionarioAdmin)
