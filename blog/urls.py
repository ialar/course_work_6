from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogPostListView, BlogPostDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('view/<int:pk>/', cache_page(60)(BlogPostDetailView.as_view()), name='blogpost_view'),
]
