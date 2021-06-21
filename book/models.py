from django.db import models


# Create your models here.
class Book(models.Model):
    book_name = models.CharField('book name', max_length=50, unique=True)
    book_writer = models.CharField('book writer', max_length=50, unique=True)
    year_of_publication = models.IntegerField('year of publication')
    registration_time = models.DateTimeField('registration time', auto_now_add=True)
    update_time = models.DateTimeField('update time', null=True)
    username = models.CharField('username', max_length=50)

    def __str__(self):
        return f'{self.book_name} write by {self.book_writer}'
