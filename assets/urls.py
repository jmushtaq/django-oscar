from django.urls import path

from . import views

urlpatterns = [
    # ex: /folio/
    path("", views.index, name="index"),
#    path("home", views.home, name="home"),
#    path("services", views.services, name="services"),
#    path("portfolio", views.portfolio, name="portfolio"),
#    path("journal", views.journal, name="journal"),
#    path("about", views.about, name="about"),
#    path("contact", views.contact, name="contact"),
#    path("blog-single", views.blog_single, name="blog_single"),
    path("browse", views.browse, name="browse"),
    path("index2", views.index2, name="index2"),
]
