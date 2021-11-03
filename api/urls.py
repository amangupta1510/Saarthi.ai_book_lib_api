from django.urls import path
from . import views

urlpatterns = [
    path('external-books', views.ExternalBook, name='external-book-detail'),
    path('books', views.CreateBook, name='book-create'),
    path('books/<int:id>', views.ViewBook, name='book-detail'),
]
