from django.db import models

# Create your models here.
class Projeto(models.Model):

    CATEGORIAS = [
        ('W', 'Web Design'),
        ('B', 'Branding'),
        ('D', 'Desenvolvimento'),
        ('M', 'Marketing')
    ]

    titulo = models.CharField(max_length=68, null=False)
    capa = models.ImageField(null=False, blank=False)
    descricao = models.TextField()
    categoria = models.CharField(max_length=1, choices=CATEGORIAS, default='W')
    publicado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo    

class ImagesProject(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    imagem = models.ImageField()
    descricao = models.CharField(max_length=55)



class Funcionario(models.Model):
    imagem = models.ImageField(blank=False)
    nome = models.CharField(max_length=100, null=False, blank=False)
    cargo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(max_length=255)
    instagram = models.CharField(max_length=168)
    facebook = models.CharField(max_length=168)
    linkedin = models.CharField(max_length=168)

    def __str__(self) -> str:
        return self.nome