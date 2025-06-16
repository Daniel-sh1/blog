from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('user/', include('users.urls')),
    path('user/', include('django.contrib.auth.urls')),

]
