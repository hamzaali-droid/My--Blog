from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.views.static import serve

urlpatterns = [
    path("", views.index, name="Home"),
    path("blog/", views.blog, name="Blog"),
    path("blogposts/", views.blogPosts, name="Posts"),
    path("blog/post/<int:id>/", views.post, name="Post"),
    path("about/", views.about, name="About"),
    path("subscribe/", views.subscribe, name="Subscribe"),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
