from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('blog/',views.blog,name='blog'),
    path('blog/<slug:blog_id>',views.blogdetail,name='blog_detail'),
    path('login/',views.login,name='login'),
]
