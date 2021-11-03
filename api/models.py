from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length= 250, null=False, blank=False)
    isbn = models.CharField(max_length=20, null=False, blank=False)
    authors = models.TextField()
    number_of_pages = models.IntegerField()
    publisher = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    release_date = models.DateField()

    def __str__(self):
        return self.name
    
