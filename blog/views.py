from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Categories, Post
from .forms import PostForm
from django.urls import reverse_lazy

# def index(request):
#     posts = Post.objects.all()

#     return render(
#         request=request, 
#         context={
#             "posts":posts,
#             }, 
#         template_name="index.html"
#         )

# For anonym User
class PostsByCategoryListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "index.html"
    paginate_by = 3
    
    def get_queryset(self):
        queryset = Post.objects.filter(categories__slug=self.kwargs['slug'])
        return queryset
    
# For anonym User
class PostsListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "index.html"
    ordering = ["-id"]
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
# For anonym User
class PostDetailView(DetailView):
    model = Post
    template_name = "singlepost.html"
    context_object_name = "post"

# For super User
class AdminPostsListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "manager.html"
    ordering = ["-id"]


# For super User
class AdminPostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "editpost.html"
    success_url = "/"


# For super User
class AdminPostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "createpost.html"
    success_url = "/"

# For super User
# class AdminPostDeleteView()
    
    

