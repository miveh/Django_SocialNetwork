from django.utils import timezone

from django.db import models
from user.models import Profile



# Create your models here.


class Book(models.Model):
    class Meta:
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب ها'

    STATUS_CHOICESE = [('F', 'free'), ('B', 'borrowed'), ('D', 'deprecated')]
    name = models.CharField('book name', max_length=50, null=True)
    writer = models.CharField('writer', max_length=50, null=True)
    image = models.ImageField('books/', blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')
    liked = models.ManyToManyField(Profile, blank=True, related_name='likes')
    publish_year = models.IntegerField('publish year', default=2021)
    recorded = models.DateTimeField('record time', default=timezone.now)
    updated = models.DateTimeField('update time', default=timezone.now)
    status = models.CharField('status', max_length=1, choices=STATUS_CHOICESE, default='F')

    def __str__(self):
        return f'{self.name} write by {self.writer}'

    def status(self):
        if self.status == 'F':
            self.status = 'B'
        else:
            self.status = 'F'
        self.save()

        return self.status

    def get_record_date(self):
        return self.recorded.year


class Comment(models.Model):
    class Meta:
        ordering = ('-created',)

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comment_owner')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    LIKE_CHOICES = [('L', 'like'), ('D', 'dislike')]
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='like_owner')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    like = models.CharField(max_length=1, choices=LIKE_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def toggle(self):
        if self.like == 'L':
            self.like = 'D'
        else:
            self.like = 'L'
        self.save()

        return self.like
