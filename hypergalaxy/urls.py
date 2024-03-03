from hypergalaxy import views
from django.urls import path

urlpatterns = [
    path('', views.index , name='index'),
    path('contato', views.contato, name='contato'),
    path('sendmail', views.send_email, name='sendemail'),
    path('sobre', views.sobre, name='sobre'),
    path('projetos', views.projetos, name='projetos'),
    path('equipe', views.equipe, name='equipe'),
    path('projeto/', views.projeto_padrao, name='projeto-padrao'),

    path('equipe/<int:colaborador_id>', views.colaborador),
    path('projetos/<int:projeto_id>', views.projeto),
]

handler404 = views.page_not_found