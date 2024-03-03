# from blog.views import Views
from blog import views
from hypergalaxy import views as Hyper_views
from django.urls import path

urlpatterns = [
    path('blog',  views.PostList.as_view(), name='blog'),
    path('blog/<slug:slug>',  views.DetailView.as_view()),
    # path('blog', Views.index, name='blog')
]

handler404 = Hyper_views.page_not_found