from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field


class Post(models.Model):

    CATEGORIA = [
        ('N', 'Notícias'),
        ('S', 'Social Mídia'),
        ('P', 'Programação')
    ]

    capa = models.ImageField(blank=False)
    titulo = models.CharField(max_length=68, null=False, blank=False)
    sumario = models.TextField(max_length=120)
    categorias = models.CharField(max_length=1, choices=CATEGORIA, default='N')
    slug = models.CharField(max_length=120, null=False, blank=False)
    conteudo = CKEditor5Field(config_name='extends')
    publicado = models.BooleanField(default=True)
    destaque = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.titulo
    