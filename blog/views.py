from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Categories, Post

# def index(request):
#     posts = Post.objects.all()

#     return render(
#         request=request, 
#         context={
#             "posts":posts,
#             }, 
#         template_name="index.html"
#         )

class PostsListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class PostsListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class PostDetailView(DetailView):
    model = Post
    template_name = "singlepost.html"
    context_object_name = "post"

