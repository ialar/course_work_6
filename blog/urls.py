from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogPostListView, BlogPostDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('view/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost_view'),
]
