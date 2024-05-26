from django.urls import path

from . import views

urlpatterns = [
    # ex: /folio/
    path("", views.index, name="index"),
    path("blog-single", views.blog_single, name="blog_single"),
]
