from django.contrib import admin
from django.urls import path

from posts.views import posts_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/',posts_list_view)
]
