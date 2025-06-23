from django.urls import path
from django.contrib.auth.views import LoginView
from .views import (
    PostsListView, 
    PostDetailView, 
    PostsByCategoryListView, 
    AdminPostUpdateView, 
    AdminPostCreateView,
    AdminPostsListView,
    AdminPostDeleteView
    )

urlpatterns = [
    # for User
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('', PostsListView.as_view(), name="index"),
    path('post/<int:pk>', PostDetailView.as_view(), name="singlepost"),
    path('category/<str:slug>', PostsByCategoryListView.as_view(), name="postbycategory"),
    # for Super User
    path('manager/post', AdminPostsListView.as_view(), name="adminpost"),
    path('manager/post/update/<int:pk>', AdminPostUpdateView.as_view(), name="admineditpost"),
    path('manager/post/create', AdminPostCreateView.as_view(), name="admincreatepost"),
    path('manager/post/delete/<int:pk>/', AdminPostDeleteView.as_view(), name="admindeletepost"),
]


