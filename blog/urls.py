from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<int:pk>/delete/", views.blog_delete, name="blog_delete"),
    path("<category>/", views.blog_category, name="blog_category"),
] 