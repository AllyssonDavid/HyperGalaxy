from typing import Any
from django.shortcuts import render
from blog.models import Post
from django.views import generic


class PostList(generic.ListView):
    queryset = Post.objects.filter(publicado=True, destaque=False).order_by('created_at')
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pagina'] = 'Blog'
        context['post_destaque'] = Post.objects.filter(publicado=True, destaque=True).first()
        return context

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail_post.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['outros_posts'] = Post.objects.filter(publicado=True, destaque=False)[:2]
        context['pagina'] = 'Blog'
        return context