from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('user/', include('users.urls')),
    path('user/', include('django.contrib.auth.urls')),

]
