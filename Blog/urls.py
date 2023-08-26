from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("blog", views.blog, name='blog'),
    path("team", views.team, name='team'),
    path("courses", views.courses, name='courses'),
    path("myblogs", views.myblogs, name='myblogs'),
    path('blog_user/<str:username>/', views.blog_user, name='blog_user')
]