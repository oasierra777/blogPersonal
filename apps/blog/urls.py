from django.urls import path

from apps.blog.views import BlogListView
from apps.blog.views import ListPostsByCategoryView
from apps.blog.views import PostDetailView
from apps.blog.views import SearchBlogView

urlpatterns = [
    path('list', BlogListView.as_view()),
    path('by_category', ListPostsByCategoryView.as_view()),
    path('detail/<slug>', PostDetailView.as_view()),
    path('search', SearchBlogView.as_view()),
]