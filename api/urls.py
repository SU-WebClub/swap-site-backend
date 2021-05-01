from django.urls import path
from .views import BlogAPIView, CategoryAPIView, TagAPIView, AuthorAPIView, SearchAPIView, NewsAPIView


urlpatterns = [
    path('blog/', BlogAPIView.as_view()),
    path('category/', CategoryAPIView.as_view()),
    path('tag/', TagAPIView.as_view()),
    path('author/', AuthorAPIView.as_view()),
    path('search/', SearchAPIView.as_view()),
    path('news/', NewsAPIView.as_view()),
]



