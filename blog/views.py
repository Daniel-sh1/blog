from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from .models import Categories, Post
from .forms import PostForm

# def index(request):
#     posts = Post.objects.all()

#     return render(
#         request=request, 
#         context={
#             "posts":posts,
#             }, 
#         template_name="index.html"
#         )

class PostsByCategoryListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "index.html"
    paginate_by = 3
    
    def get_queryset(self):
        queryset = Post.objects.filter(categories__slug=self.kwargs['slug'])
        return queryset
    

class PostsListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "index.html"
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class PostDetailView(DetailView):
    model = Post
    template_name = "singlepost.html"
    context_object_name = "post"


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "editpost.html"
    success_url = "/"
    
    

