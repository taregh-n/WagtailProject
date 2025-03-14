from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import DjBlogModel
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import DjBlogSerializer
from django.shortcuts import get_object_or_404

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
        serializer = DjBlogSerializer(posts, many=True)
        return Response(serializer.data)

# ViewSet api
class BlogViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = DjBlogModel.objects.all()
        serializer = DjBlogSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = DjBlogModel.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = DjBlogSerializer(post)
        return Response(serializer.data)