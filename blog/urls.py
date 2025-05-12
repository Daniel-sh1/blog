from django.urls import path
from .views import PostsListView, PostDetailView, PostsByCategoryListView

urlpatterns = [
    path('', PostsListView.as_view(), name="index"),
    path('post/<int:pk>', PostDetailView.as_view(), name="singlepost"),
    path('category/<str:slug>', PostsByCategoryListView.as_view(), name="postbycategory")

]


