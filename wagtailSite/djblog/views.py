from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import DjBlogModel
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.

class BlogListView(ListView):
    model = DjBlogModel
    template_name = "djblog/dj_blog_model.html"

class BlogDetailView(DetailView):
    model = DjBlogModel
    template_name = "djblog/blog_detail.html"

class BlogEditView(UpdateView):
    model = DjBlogModel
    template_name = "djblog/edit_blog.html"
    fields = ["title"]
    success_url = "/djblog/"

class BlogCreateView(CreateView):
    model = DjBlogModel
    template_name = "djblog/add_blog.html"
    fields = ["title"]
    success_url = "/djblog/"

class BlogAPI(APIView):
    def get(self, request, format=None):
        posts = DjBlogModel.objects.all()
        res = [post.title for post in posts]
        return Response(res)