from django.urls import path

from apps.category.views import ListCategoriesView

urlpatterns = [
    path('list', ListCategoriesView.as_view()),
]