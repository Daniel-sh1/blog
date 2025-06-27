from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Categories, Post
from .forms import PostForm
from .mixins import AccessMixin

# For anonym User
class PostsByCategoryListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "index.html"
    paginate_by = 3
    
    def get_queryset(self):
        queryset = Post.objects.filter(categories__slug=self.kwargs['slug'], publish=True)
        return queryset
    
# For anonym User
class PostsListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "index.html"
    ordering = ["-id"]
    paginate_by = 3

    def get_queryset(self):
        queryset = Post.objects.filter(publish=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
# For anonym User
class PostDetailView(DetailView):
    model = Post
    template_name = "singlepost.html"
    context_object_name = "post"

# For staff User (изменено с superuser на staff)
class AdminPostsListView(AccessMixin, ListView):
    model = Post
    context_object_name = "posts"
    template_name = "manager.html"
    ordering = ["-id"]

    # "admin", "manager", "user"
    allowed_roles = ['admin',]



class AdminPostUpdateView(AccessMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "editpost.html"
    success_url = "/"

    allowed_roles = ['admin',]


class AdminPostCreateView(AccessMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "createpost.html"
    success_url = "/"
    
    allowed_roles = ['admin',]



class AdminPostDeleteView(AccessMixin, DeleteView):
    model = Post
    template_name = "deletepost.html"
    context_object_name = "post"
    success_url = "/"
    allowed_roles = ['admin',]


