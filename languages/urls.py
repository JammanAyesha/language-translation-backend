from django.urls import path
from .views import language_list

urlpatterns = [
    path('', language_list, name='language-list')
]