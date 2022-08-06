"""practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from myapp.views import index,create,detail,result
from blog.views import ArticleListView,ArticleDetailView,ArticleCreateView
from blog.views import ArticleUpdateView
from blog.views import ArticleDeleteView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('create/',create,name='create'),
    path('detail/<str:slug>',detail,name='detail'),
    path('results',result,name='results'),
    path('blog',ArticleListView.as_view(),name='blog_index'),
    path('blog/<int:id>',ArticleDetailView.as_view(),name='detail_view'),
    path('blog/create',ArticleCreateView.as_view(),name='create_article'),
    path('blog/update/<int:id>',ArticleUpdateView.as_view(),name='update_article'),
    path('blog/delete/<int:id>',ArticleDeleteView.as_view(),name='delete_article')
]
