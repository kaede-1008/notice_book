from django.db import models

# Create your models here.

class Post(models.Model):
    book_title = models.CharField(max_length=255)
    book_auther = models.CharField(max_length=255)
    book_illust = models.CharField(max_length=255)
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_title

class Book(models.Model):
    book_title = models.CharField(max_length=255)
    book_auther = models.CharField(max_length=255)
    book_illust = models.CharField(max_length=255)
    publish_date = models.CharField(max_length=255)
