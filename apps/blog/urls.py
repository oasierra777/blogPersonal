from django.urls import path

from apps.blog.views import BlogListView
from apps.blog.views import ListPostsByCategoryView

urlpatterns = [
    path('list', BlogListView.as_view()),
    path('by_category', ListPostsByCategoryView.as_view()),
]