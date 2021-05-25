from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Blog, Category, Tag, Author, News
from .serializers import BlogSerializer, CategorySerializer, TagSerializer, AuthorSerializer, SearchSerializer, NewsSerializer
from rest_framework import filters


class BlogAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('id', 'category__slug', 'tags', 'author')

class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('id', 'slug')

class TagAPIView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class AuthorAPIView(ListAPIView):
    queryset = Author.objects.order_by('role')
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('id', 'role__name')

class SearchAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = SearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'tags__name', 'content', 'author__name', 'category__name']

class NewsAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('id',)
