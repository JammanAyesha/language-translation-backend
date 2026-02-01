from django.urls import path
from .views import add_favorite, list_favorites, delete_favorite

urlpatterns = [
    path('', list_favorites),
    path('add/', add_favorite),
    path('<int:pk>/', delete_favorite),
]