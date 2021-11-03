from django.urls import path
from . import views

urlpatterns = [
    path('external-books', views.ExternalBook, name='external-book-detail'),
    path('v1/books', views.CreateBook, name='book-create'),
    path('v1/books/<int:id>', views.ViewBook, name='book-detail'),
]
